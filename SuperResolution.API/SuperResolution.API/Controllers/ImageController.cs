using System;
using System.Collections.Generic;
using System.IO;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Http.Internal;
using Microsoft.AspNetCore.Mvc;
using SuperResolution.API.PythonExecutor;

namespace SuperResolution.API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ImageController : ControllerBase
    {
        private IFormFile image;
        private string imagePath = "\"C:/git/SuperRes/super_resolution/out.jpeg\"";

        // GET: api/Image
        [HttpGet]
        public IFormFile Get()
        {
            return this.image;
        }

        // POST: api/Image
        [HttpPost]
        public IActionResult Post([FromBody] string value)
        {
//            MLSharpPython ml = new MLSharpPython("C:/Users/mi6o_/AppData/Local/Programs/Python/Python37/python.exe");
            MLSharpPython ml = new MLSharpPython("C:/Users/Eti Tsvetkova/AppData/Local/Programs/Python/Python37/python.exe");
            string error = string.Empty;
            //ml.ExecutePythonScript("", out error);
            //            ml.ExecutePythonScript("\"B:/Visual Studio Projects/SuperRes/super_resolution/super_resolve.py\"" +
            //                                   " --model_pth \"B:/Visual Studio Projects/SuperRes/super_resolution/model-basic.pth\"" +
            //                                   " --input_image \"B:/Visual Studio Projects/SuperRes/super_resolution/out.jpeg\"", out error);

            ml.ExecutePythonScript("\"C:/git/SuperRes/super_resolution/super_resolve.py\"" +
                                   " --model_pth \"C:/git/SuperRes/super_resolution/model-basic.pth\"" +
                                    " --input_image " + this.imagePath, out error);
            using (var stream = System.IO.File.OpenRead(this.imagePath))
            {
                this.image = new FormFile(stream, 0, stream.Length, null, Path.GetFileName(stream.Name))
                {
                    Headers = new HeaderDictionary(),
                    ContentType = "image/jpeg"
                };
            }
            Console.WriteLine(error);
            return this.Ok();
        }
    }
}
