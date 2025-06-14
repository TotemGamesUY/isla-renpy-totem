; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "La Isla"
#define MyAppVersion "1"
#define MyAppPublisher "Totem Games"
#define MyAppURL "https://www.totemgames.org/"
#define MyAppExeName "La_Isla.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{AFFE0E04-4EA6-4A5A-91D9-9885AFEE8CBC}}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={userdesktop}\La_IslaTest
UninstallDisplayIcon={app}\{#MyAppExeName}
; "ArchitecturesAllowed=x64compatible" specifies that Setup cannot run
; on anything but x64 and Windows 11 on Arm.
ArchitecturesAllowed=x64compatible
; "ArchitecturesInstallIn64BitMode=x64compatible" requests that the
; install be done in "64-bit mode" on x64 or Windows 11 on Arm,
; meaning it should use the native 64-bit Program Files directory and
; the 64-bit view of the registry.
ArchitecturesInstallIn64BitMode=x64compatible
DefaultGroupName={#MyAppName}
; Remove the following line to run in administrative install mode (install for all users).
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputBaseFilename=mysetup
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\renpy\renpy-8.3.7-sdk\La_Isla-0.8-dists\La_Isla-0.8-pc\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\renpy\renpy-8.3.7-sdk\La_Isla-0.8-dists\La_Isla-0.8-pc\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "idp.dll"; DestDir: "{tmp}"; Flags: ignoreversion dontcopy

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

[Code]

var
  IDPage: TInputQueryWizardPage;
  IDEdit: TEdit;

const
  ITD_DLL = 'idp.dll';

type
  TDownloadCallback = function(Progress, ProgressMax: Integer; StatusText: PAnsiChar): Integer;

function DownloadTemporaryFile(const URL, Filename, UserAgent: String; Callback: TDownloadCallback): Integer;
  external 'DownloadTemporaryFile@files:idp.dll stdcall delayload';

// Dummy callback function
function DownloadCallback(Progress, ProgressMax: Integer; StatusText: PAnsiChar): Integer;
begin
  // Return 0 to continue, 1 to cancel
  Result := 0;
end;

function DownloadValidIDs(): Boolean;
var
  CSVResponseFile: string;
  WinHttpReq: Variant;
begin
  CSVResponseFile := ExpandConstant('{tmp}\valid_ids.csv');
  
  try
    // Create HTTP request object
    WinHttpReq := CreateOleObject('WinHttp.WinHttpRequest.5.1');
    
    // Configure request
    WinHttpReq.Open('GET', 
      'https://docs.google.com/spreadsheets/d/1t3SZc7Ab1vd8cTYOLH-Yd3fTtQqVNJ1esFWw78fe5W0/export?format=csv&gid=0', 
      False);
    
    // Set headers to mimic a browser request
    WinHttpReq.SetRequestHeader('User-Agent', 'Mozilla/5.0');
    WinHttpReq.SetRequestHeader('Accept', '*/*');
    
    // Send the request
    WinHttpReq.Send();
    
    // Check if request was successful
    if WinHttpReq.Status = 200 then
    begin
      // Save response to file
      SaveStringToFile(CSVResponseFile, WinHttpReq.ResponseText, False);
      Result := True;
    end
    else
    begin
      MsgBox('Error al descargar: Código ' + IntToStr(WinHttpReq.Status), mbError, MB_OK);
      Result := False;
    end;
  except
    MsgBox('Excepción al descargar la lista de IDs.', mbError, MB_OK);
    Result := False;
  end;
  
  if not Result then
    MsgBox('No se pudo descargar la lista de IDs.', mbError, MB_OK);
end;

function IsValidID(ID: string): Boolean;
var
  CSVFile: string;
  Lines: TArrayOfString;
  i: Integer;
  CurrentLine: string;
  CurrentID: string;
  PlayerIDFile: string;
begin
  Result := False;
  CSVFile := ExpandConstant('{tmp}\valid_ids.csv');
  
  if not FileExists(CSVFile) then
  begin
    MsgBox('No se encontró el archivo de IDs válidos.', mbError, MB_OK);
    Exit;
  end;

  if LoadStringsFromFile(CSVFile, Lines) then
  begin
    for i := 0 to GetArrayLength(Lines) - 1 do
    begin
      CurrentLine := Lines[i];
      
      if Pos(',', CurrentLine) > 0 then
      begin
        CurrentID := Trim(Copy(CurrentLine, 1, Pos(',', CurrentLine) - 1));
        
        if CurrentID = ID then
        begin
          Result := True;
          PlayerIDFile := ExpandConstant('{localappdata}\LaIsla\player_id.txt');
          ForceDirectories(ExtractFilePath(PlayerIDFile));
          SaveStringToFile(PlayerIDFile, ID, False);
          Break; // Termina el bucle si encuentra el ID
        end;
      end;
    end;
  end
  else
    MsgBox('Error al leer el archivo de IDs.', mbError, MB_OK);
end;

function CheckIDValid(Sender: TWizardPage): Boolean;
var
  PlayerID: string;
begin
  // Access the input value through the page's Edits array
  PlayerID := Trim(IDPage.Values[0]);
  Result := True;

  if PlayerID = '' then
  begin
    MsgBox('Debes ingresar un ID.', mbError, MB_OK);
    Result := False;
    Exit;
  end;

  if not IsValidID(PlayerID) then
  begin
    MsgBox('ID no válido. Contacta al administrador.', mbError, MB_OK);
    Result := False;
  end;
end;

procedure InitializeWizard;
begin
  
  IDPage := CreateInputQueryPage(wpWelcome, 'Registro', 'Introduce tu ID',
    'Por favor introduce tu ID para continuar:');

  IDEdit := IDPage.Add('ID del jugador:', False);

  if not DownloadValidIDs() then
    MsgBox('Error al conectar con la base de datos de IDs.', mbError, MB_OK);

  IDPage.OnNextButtonClick := @CheckIDValid;
end;


