{
	description = "Day Planner and Investment Tracker";

	inputs = {
		nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
		flake-utils.url = "github:numtide/flake-utils";
	};

	outputs = { self, nixpkgs, flake-utils }:
		flake-utils.lib.eachDefaultSystem (system:
				let
				pkgs = import nixpkgs { inherit system; };
				in {
				devShell = pkgs.mkShell {                                                                  
				name = "day-planner-env";
				buildInputs = with pkgs; [
          curl
				  python311
# Project Lib
				python311Packages.pip
				  python311Packages.pandas
          python311Packages.openpyxl
				python311Packages.matplotlib
				python311Packages.flask
# Emacs pyIDE libs
				python311Packages.jedi
				python311Packages.black
				python311Packages.flake8
				python311Packages.sentinel
				python311Packages.python-lsp-server
				python311Packages.virtualenv
				python311Packages.pyflakes  # Linter Pyflakes
				direnv
				];                
				shellHook = ''                                                                           
					echo "Welcome to the Day Planner and Investment Tracker environment!"                    
					'';                                                                                      
				};                                                                                         
				}
				);
}
