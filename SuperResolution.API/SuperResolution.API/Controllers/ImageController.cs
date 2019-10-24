using System;
using System.IO;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using SuperResolution.API.PythonExecutor;

namespace SuperResolution.API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ImageController : ControllerBase
    {
        // GET: api/Image
        [HttpGet]
        public async System.Threading.Tasks.Task<IActionResult> GetAsync()
        {
            return File(await System.IO.File.ReadAllBytesAsync(Constants.OutputImage), "image/jpeg");
        }

        // POST: api/Image
        [HttpPost]
        public async System.Threading.Tasks.Task<IActionResult> PostAsync([FromForm]IFormFile image, [FromForm]string scale)
        {
            MLSharpPython ml = new MLSharpPython();
            if (System.IO.File.Exists(Constants.InputImage))
            {
                System.IO.File.Delete(Constants.InputImage);
            }
            using (var fileStream = new FileStream(Constants.InputImage, FileMode.Create))
            {
                await image.CopyToAsync(fileStream);
            }

            string error = string.Empty;
            ml.ExecutePythonScript("../../super_resolution/super_resolve.py " +
                                   $"--model_pth \"{Constants.ModelBasic}\" " +
                                   $"--input_image \"{Constants.InputImage}\" " +
                                   $"--output_image \"{Constants.OutputImage}\" " +
                                   $"--scale {scale}", out error);

            Console.WriteLine(error);

            return this.Ok();
        }
    }
}
