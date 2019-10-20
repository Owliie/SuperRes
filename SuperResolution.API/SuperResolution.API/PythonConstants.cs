using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace SuperResolution.API
{
    public static class Constants
    {
        public static string DataFolder = Path.Combine(Directory.GetCurrentDirectory(), "Data");
        public static string ModelBasic = Path.Combine(DataFolder, "model-basic.pth");
        public static string InputImage = Path.Combine(DataFolder, "in.jpg");
        public static string OutputImage = Path.Combine(DataFolder, "out.jpg");
    }
}
