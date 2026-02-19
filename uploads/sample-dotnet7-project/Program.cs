using Microsoft.AspNetCore.Builder;
using Microsoft.Extensions.Hosting;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddMvc();
builder.Services.AddAuthentication();

var app = builder.Build();

app.UseEndpoints(endpoints =>
{
    endpoints.MapControllers();
});

app.Run();
