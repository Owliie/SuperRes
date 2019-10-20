using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;
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

        // GET: api/Image
        [HttpGet]
        public IFormFile Get()
        {
            return this.image;
        }

        // POST: api/Image
        [HttpPost]
        public IActionResult Post([FromForm]IFormFile image)
        {
            MLSharpPython ml = new MLSharpPython();
            if (System.IO.File.Exists(Constants.InputImage))
            {
                System.IO.File.Delete(Constants.InputImage);
            }
            using (var fileStream = new FileStream(Constants.InputImage, FileMode.Create))
            {
                image.CopyTo(fileStream);
            }

            string error = string.Empty;
            ml.ExecutePythonScript("../../super_resolution/super_resolve.py " +
                                   $"--model_pth \"{Constants.ModelBasic}\" " +
                                   $"--input_image \"{Constants.InputImage}\" " +
                                   $"--output_image \"{Constants.OutputImage}\"", out error);

            Console.WriteLine(error);

            return this.Ok();
        }
    }
}
