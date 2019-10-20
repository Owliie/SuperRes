using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using SuperResolution.API.PythonExecutor;

namespace SuperResolution.API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ValuesController : ControllerBase
    {
        // GET api/values
        [HttpGet]
        public ActionResult<IEnumerable<string>> Get()
        {
            MLSharpPython ml = new MLSharpPython("C:/Users/mi6o_/AppData/Local/Programs/Python/Python37/python.exe");
            string error = string.Empty;
            //ml.ExecutePythonScript("", out error);
            ml.ExecutePythonScript("\"B:/Visual Studio Projects/SuperRes/super_resolution/super_resolve.py\"" +
                " --model_pth \"B:/Visual Studio Projects/SuperRes/super_resolution/model-basic.pth\"" +
                " --input_image \"B:/Visual Studio Projects/SuperRes/super_resolution/out.jpeg\"", out error);
            Console.WriteLine(error);
            return new string[] { "value1", "value2" };
        }

        // GET api/values/5
        [HttpGet("{id}")]
        public ActionResult<string> Get(int id)
        {
            return "value";
        }

        // POST api/values
        [HttpPost]
        public void Post([FromBody] string value)
        {
        }

        // PUT api/values/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] string value)
        {
        }

        // DELETE api/values/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}
