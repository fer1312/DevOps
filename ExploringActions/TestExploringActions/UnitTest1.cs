using ExploringActions.Controllers;
using Xunit;
using Microsoft.AspNetCore.Mvc;
using System.Linq;

namespace TestExploringActions
{
    public class WeatherForecastControllerTest
    {
        [Fact]
        public void Get_ReturnsValues()
        {
            // Arrange
            var controller = new WeatherForecastController(null);

            // Act
            var result = controller.Get();

            // Assert
            Assert.NotNull(result);
            Assert.True(result.Any());
        }
    }
}
