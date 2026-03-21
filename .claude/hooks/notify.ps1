Add-Type -AssemblyName System.Windows.Forms

# C# 스레드로 beep 루프 실행 (Runspace 타이밍 문제 회피)
Add-Type -TypeDefinition @'
using System;
using System.Runtime.InteropServices;
using System.Threading;

public class BeepHelper {
    [DllImport("kernel32.dll")]
    public static extern bool Beep(uint dwFreq, uint dwDuration);

    private static Thread _thread;
    private static volatile bool _running;

    public static void Start() {
        _running = true;
        _thread = new Thread(() => {
            while (_running) {
                Beep(800, 400);
                Thread.Sleep(600);
            }
        });
        _thread.IsBackground = true;
        _thread.Start();
    }

    public static void Stop() {
        _running = false;
    }
}
'@

[BeepHelper]::Start()

# Show popup (blocks until OK is clicked)
[System.Windows.Forms.MessageBox]::Show(
    "Claude Code task completed.`nClick OK to dismiss.",
    "Claude Code Notification",
    [System.Windows.Forms.MessageBoxButtons]::OK,
    [System.Windows.Forms.MessageBoxIcon]::Information
) | Out-Null

[BeepHelper]::Stop()
