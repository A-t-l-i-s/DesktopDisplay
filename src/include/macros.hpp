#pragma once


#define PROGRAM_FILE_WINDOWED "DesktopDisplay.exe"
#define PROGRAM_FILE_DEBUG "DesktopDisplay_Debug.exe"
#define PROGRAM_FILE_TASK "DesktopDisplay_Task.exe"




// ~~~~~~~~~ Program Name ~~~~~~~~~
#if defined(DEBUG)
	#define PROGRAM_NAME "DesktopDisplay Debug"
#elif defined(TASK)
	#define PROGRAM_NAME "DesktopDisplay Task"
#else
	#define PROGRAM_NAME "DesktopDisplay"
#endif
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


// ~~~~~~~~~ Program File ~~~~~~~~~
#if defined(DEBUG)
	#define PROGRAM_FILE PROGRAM_FILE_DEBUG
#elif defined(TASK)
	#define PROGRAM_FILE PROGRAM_FILE_TASK
#else
	#define PROGRAM_FILE PROGRAM_FILE_WINDOWED
#endif
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


// ~~~~~~~~~ Program Icon ~~~~~~~~~
#if defined(DEBUG)
	#define PROGRAM_ICON "icon_debug.ico"
#elif defined(TASK)
	#define PROGRAM_ICON "icon_task.ico"
#else
	#define PROGRAM_ICON "icon.ico"
#endif
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#define COMPANY_NAME "Atlis"
#define PROGRAM_COPYRIGHT "Copyright (C) Atlis"

#define PROGRAM_VERSION "1.0.0"
#define PROGRAM_VERSION_ID 1,0,0

#define PROGRAM_REGEX "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
#define PROGRAM_REGEX_NAME "DesktopDisplay"

