#pragma once

#include<require.hpp>



namespace Path{
	// ~~~~~~~~~~~ Variables ~~~~~~~~~~
	bool ready = false;

	fs::path binPath;
	fs::path exePath;
	fs::path programPath;
	// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	// ~~~~~~~~~~~~ Define ~~~~~~~~~~~~
	void setup();
	string child(string);
	wstring childW(string);
	// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



	void setup(){
		if (not ready){
			{
				// Allocate vars
				char exePath_[PATH_MAX];
				
				// Get path
				GetModuleFileName(NULL, exePath_, PATH_MAX);

				exePath = fs::path(exePath_);
			}

			programPath = exePath.parent_path();
			binPath = programPath / "bin";


			// Change working directory
			fs::current_path(programPath);


			// Add dll directory
			AddDllDirectory(
				binPath.generic_wstring().c_str()
			);


			// Allocate instances directory
			{
				fs::path path = "insts";
				fs::create_directories(path);
			}


			// Set done
			Path::ready = true;
		}
	}



	string child(string name){
		return (programPath / name).generic_string();
	}

	wstring childW(string name){
		return (programPath / name).generic_wstring();
	}
};
