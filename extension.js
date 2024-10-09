const vscode = require('vscode'); // Imports the VS Code API to interact with the editor's features and functionality.
const path = require('path'); // Imports the Node.js 'path' module to work with file and directory paths.

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {

    // First command: Generate README for the current Jupyter Notebook
    let disposable1 = vscode.commands.registerCommand('extension.runTask1', function () {
        // Get the currently active file's editor
        const activeEditor = vscode.window.activeTextEditor;
        
        if (activeEditor) {
            const notebookFilePath = activeEditor.document.fileName;

            // Check if the file is a .ipynb (Jupyter Notebook)
            if (notebookFilePath.endsWith('.ipynb')) {
                // Get the path to the Python script in the extension's root directory
                const pythonFilePath = path.join(__dirname, 'python-scripts', 'feature_readme_generator.py');

                // Create a new terminal
                const terminal = vscode.window.createTerminal("Python Terminal");
        
                // Run the Python script and pass the Jupyter Notebook's path
                terminal.show();
                terminal.sendText(`python "${pythonFilePath}" "${notebookFilePath}"`);
            } else {
                vscode.window.showErrorMessage("Please open a Jupyter Notebook (.ipynb) file.");
            }
        } else {
            vscode.window.showErrorMessage("No active editor found.");
        }
    });

    // Second command: Select a folder and generate README files for all Jupyter Notebooks
    let disposable2 = vscode.commands.registerCommand('extension.runTask2', function () {
        // Let the user select a folder
        vscode.window.showOpenDialog({
            canSelectFolders: true,
            canSelectMany: false,
            openLabel: 'Select folder containing all Jupyter Notebooks'
        }).then(folderUri => {
            if (folderUri && folderUri[0]) {
                const directoryPath = folderUri[0].fsPath;

                // Get the path to the Python script in the extension's root directory
                const pythonFilePath = path.join(__dirname, 'python-scripts', 'feature_readme_auto_generator.py');

                // Create a new terminal
                const terminal = vscode.window.createTerminal("Python Terminal");

                // Run the Python script and pass the selected folder path
                terminal.show();
                terminal.sendText(`python "${pythonFilePath}" "${directoryPath}"`);
            } else {
                vscode.window.showErrorMessage("No folder selected.");
            }
        });
    });

     // Third command: Generate README for the current Groovy file
	 let disposable3 = vscode.commands.registerCommand('extension.runTask3', function () {
        // Get the currently active Groovy file
        const activeEditor = vscode.window.activeTextEditor;

        if (activeEditor) {
            const groovyFilePath = activeEditor.document.fileName;
            if (groovyFilePath.endsWith('.groovy')) {
                // Let the user select a folder for saving the README files
                vscode.window.showOpenDialog({
                    canSelectFolders: true,
                    canSelectMany: false,
                    openLabel: 'Select folder containing feature README files'
                }).then(folderUri => {
                    if (folderUri && folderUri[0]) {
                        const readmeDirectory = folderUri[0].fsPath;
                        const pythonFilePath = path.join(__dirname, 'python-scripts', 'pipeline_readme_generator.py');
                        const terminal = vscode.window.createTerminal("Python Terminal");

                        // Run the Python script and pass the Groovy file path and the directory for saving the README files
                        terminal.show();
                        terminal.sendText(`python "${pythonFilePath}" "${groovyFilePath}" "${readmeDirectory}"`);
                    } else {
                        vscode.window.showErrorMessage("No folder selected for README files.");
                    }
                });
            } else {
                vscode.window.showErrorMessage("Please open a Groovy (.groovy) file.");
            }
        } else {
            vscode.window.showErrorMessage("No active editor found.");
        }
    });

	// Fourth command: Generate README for all Groovy files in a selected folder
	let disposable4 = vscode.commands.registerCommand('extension.runTask4', function () {
		// Step 1: Let the user select a folder containing Groovy files
		vscode.window.showOpenDialog({
			canSelectFolders: true,
			canSelectMany: false,
			openLabel: 'Select folder containing all Groovy files'
		}).then(groovyFolderUri => {
			if (groovyFolderUri && groovyFolderUri[0]) {
				const groovyDirectory = groovyFolderUri[0].fsPath;

				// Step 2: Let the user select a folder for saving the README files
				vscode.window.showOpenDialog({
					canSelectFolders: true,
					canSelectMany: false,
					openLabel: 'Select folder containing feature README files'
				}).then(readmeFolderUri => {
					if (readmeFolderUri && readmeFolderUri[0]) {
						const readmeDirectory = readmeFolderUri[0].fsPath;
						const pythonFilePath = path.join(__dirname, 'python-scripts', 'pipeline_readme_auto_generator.py');

						// Create a new terminal and run the Python script
						const terminal = vscode.window.createTerminal("Python Terminal");
						terminal.show();
						terminal.sendText(`python "${pythonFilePath}" "${groovyDirectory}" "${readmeDirectory}"`);
					} else {
						vscode.window.showErrorMessage("No folder selected for README files.");
					}
				});
			} else {
				vscode.window.showErrorMessage("No folder selected for Groovy files.");
			}
		});
	});

    // Command to download Jupyter Notebook files
    let disposable5 = vscode.commands.registerCommand('extension.downloadNotebooks', function () {
        // Prompt the user to input GitHub token and organization name
        vscode.window.showInputBox({ prompt: 'Enter your GitHub token' }).then(token => {
            if (!token) {
                vscode.window.showErrorMessage('GitHub token is required.');
                return;
            }

            vscode.window.showInputBox({ prompt: 'Enter the GitHub organization name' }).then(org_name => {
                if (!org_name) {
                    vscode.window.showErrorMessage('GitHub organization name is required.');
                    return;
                }

                // Let the user select a folder to save the downloaded files
                vscode.window.showOpenDialog({
                    canSelectFolders: true,
                    canSelectMany: false,
                    openLabel: 'Select folder to save downloaded files'
                }).then(folderUri => {
                    if (!folderUri || !folderUri[0]) {
                        vscode.window.showErrorMessage('No folder selected.');
                        return;
                    }

                    const downloadPath = folderUri[0].fsPath;

                    /// Prompt the user to input the max number of downloads
                    vscode.window.showInputBox({ prompt: 'Enter max downloads (integer)', validateInput: value => isNaN(value) ? 'Please enter a number' : null }).then(maxDownloads => {
                        const pythonFilePath = path.join(__dirname, 'python-scripts', 'download.py');
                        const terminal = vscode.window.createTerminal("Python Terminal");
                        terminal.show();
                        terminal.sendText(`python "${pythonFilePath}" notebook "${token}" "${org_name}" "${downloadPath}" ${maxDownloads}`);
                    });
                });
            });
        });
    });

    // Command to download Groovy Pipeline files
    let disposable6 = vscode.commands.registerCommand('extension.downloadPipelines', function () {
        // Prompt the user to input GitHub token and organization name
        vscode.window.showInputBox({ prompt: 'Enter your GitHub token' }).then(token => {
            if (!token) {
                vscode.window.showErrorMessage('GitHub token is required.');
                return;
            }

            vscode.window.showInputBox({ prompt: 'Enter the GitHub organization name' }).then(org_name => {
                if (!org_name) {
                    vscode.window.showErrorMessage('GitHub organization name is required.');
                    return;
                }

                // Let the user select a folder to save the downloaded files
                vscode.window.showOpenDialog({
                    canSelectFolders: true,
                    canSelectMany: false,
                    openLabel: 'Select folder to save downloaded files'
                }).then(folderUri => {
                    if (!folderUri || !folderUri[0]) {
                        vscode.window.showErrorMessage('No folder selected.');
                        return;
                    }

                    const downloadPath = folderUri[0].fsPath;

                    // Prompt the user to input the max number of downloads
                    vscode.window.showInputBox({ prompt: 'Enter max downloads (integer)', validateInput: value => isNaN(value) ? 'Please enter a number' : null }).then(maxDownloads => {
                        const pythonFilePath = path.join(__dirname, 'python-scripts', 'download.py');
                        const terminal = vscode.window.createTerminal("Python Terminal");
                        terminal.show();
                        terminal.sendText(`python "${pythonFilePath}" pipeline "${token}" "${org_name}" "${downloadPath}" ${maxDownloads}`);
                    });
                });
            });
        });
    });

    context.subscriptions.push(disposable1);
    context.subscriptions.push(disposable2);
    context.subscriptions.push(disposable3);
	context.subscriptions.push(disposable4);
    context.subscriptions.push(disposable5);
    context.subscriptions.push(disposable6);
}

function deactivate() {}

module.exports = {
    activate,
    deactivate
};
