; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "ARCed"
#define MyAppVersion "0.0.1"
#define MyAppPublisher "ARC Developers"
#define MyAppURL "http://www.chaos-project.com/"
#define MyAppExeName "ARCed.exe"
; file association
#define FileAssoName "ARC.Project"
#define FileAssoExt ".arcproj"
#define FileAssoDefaultIconPos "1"
; files
#define ARCMainExe "C:\Users\Ben\Desktop\ARC\editor\ARCed\build\dist\ARCed.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{00679747-F3CC-4A43-B097-D3E2F493A7E3}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={pf}\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=test.txt
InfoBeforeFile=test.txt
InfoAfterFile=test.txt
OutputBaseFilename=ARCed-setup
SetupIconFile=C:\Users\Ben\Desktop\ARC\editor\ARCed\icon.ico
Compression=lzma
SolidCompression=yes
ChangesAssociations=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked
Name: "quicklaunchicon"; Description: "{cm:CreateQuickLaunchIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked; OnlyBelowVersion: 0,6.1

[Files]
Source: "{#ARCMainExe}"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{commondesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon
Name: "{userappdata}\Microsoft\Internet Explorer\Quick Launch\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: quicklaunchicon

[Registry]
; file association
Root: HKCR; Subkey: "{#FileAssoExt}"; ValueType: string; ValueName: ""; ValueData: "{#FileAssoName}"; Flags: uninsdeletevalue
Root: HKCR; Subkey: "{#FileAssoName}"; ValueType: string; ValueName: ""; ValueData: "ARC Project File"; Flags: uninsdeletekey
Root: HKCR; Subkey: "{#FileAssoName}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\{#MyAppName},{#FileAssoDefaultIconPos}"
Root: HKCR; Subkey: "{#FileAssoName}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\{#MyAppName}"" ""%1"""
; set compatability mode
Root: HKLM; Subkey: "Software\Microsoft\Windows NT\CurrentVersion\AppCompatFlags\Layers"; ValueType: string; ValueName: "{app}\{#MyAppExeName}"; ValueData: "WINXPSP2"; Flags: uninsdeletekey;  MinVersion: 0,6.0.6000


[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, "&", "&&")}}"; Flags: nowait postinstall skipifsilent
