#pragma once

#define PY_SSIZE_T_CLEAN

#include<stdio.h>
#include<wchar.h>
#include<limits.h>
#include<stdint.h>
#include<unistd.h>
#include<stdbool.h>


#include<format>
#include<string>
#include<fstream>
#include<filesystem>

#include<python.h>
#include<windows.h>



using std::string;
using std::wstring;

namespace fs = std::filesystem;



const char* programName = "DesktopDisplay";
const char* programVersion = "1.0.0";

