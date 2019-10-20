namespace SuperResolution.API.PythonExecutor
{
    public interface IMLSharpPython
    {
        string ExecutePythonScript(string filePythonScript, out string standardError);
    }
}
