#pragma once

#include<require.hpp>
#include<path.hpp>



namespace Startup{
	void setup(){
		HKEY hKey;
		LONG result;

		result = RegOpenKeyExA(
			HKEY_CURRENT_USER,
			"Software\\Microsoft\\Windows\\CurrentVersion\\Run",
			0, 
			KEY_ALL_ACCESS,
			&hKey
		);

		if (result == ERROR_SUCCESS){
			string path = "\"" + Path::exePath.string() + "\"";

			uint16_t size = path.size();
			const uint8_t* value = (const uint8_t*)path.c_str();


			RegSetValueExA(
				hKey,
				programName,
				0,
				REG_SZ,
				value,
				size
			);

			RegCloseKey(hKey);
		}
	}
}

