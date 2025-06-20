
!define ZIP2EXE_NAME "DesktopDisplay"
!define ZIP2EXE_OUTFILE "DesktopDisplay_Installer.exe"

!define ZIP2EXE_COMPRESSOR_ZLIB
!define ZIP2EXE_INSTALLDIR "$ProgramFiles\Atlis\DesktopDisplay"

!include "${NSISDIR}\Contrib\zip2exe\Base.nsh"
!include "${NSISDIR}\Contrib\zip2exe\Classic.nsh"


!insertmacro SECTION_BEGIN
	File /r build\*
	
	AccessControl::GrantOnFile "$INSTDIR" "(BU)" "GenericRead + GenericWrite"

	Exec "$INSTDIR\DesktopDisplay.exe"
!insertmacro SECTION_END

