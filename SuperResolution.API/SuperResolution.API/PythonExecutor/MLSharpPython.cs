using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;

namespace SuperResolution.API.PythonExecutor
{
    public class MLSharpPython : IMLSharpPython
    {
        private readonly string filePythonExePath;

        public MLSharpPython(string exePythonPath = "python")
        {
            filePythonExePath = exePythonPath;
        }
        public string ExecutePythonScript(string filePythonScript, out string standardError)
        {
            string outputText = string.Empty;
            standardError = string.Empty;
            try
            {
                using (Process process = new Process())
                {
                    process.StartInfo = new ProcessStartInfo(filePythonExePath)
                    {
                        Arguments = filePythonScript,
                        UseShellExecute = false,
                        RedirectStandardOutput = true,
                        RedirectStandardError = true,
                        CreateNoWindow = true
                    };
                    process.Start();
                    outputText = process.StandardOutput.ReadToEnd();
                    outputText = outputText.Replace(Environment.NewLine, string.Empty);
                    standardError = process.StandardError.ReadToEnd();
                    process.WaitForExit();
                }
            }
            catch (Exception ex)
            {
                string exceptionMessage = ex.Message;
            }

            return outputText;
        }
    }
}
