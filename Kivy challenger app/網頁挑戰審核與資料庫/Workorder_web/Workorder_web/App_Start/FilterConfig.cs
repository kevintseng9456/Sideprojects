using System.Web;
using System.Web.Mvc;

namespace Workorder_web
{
    public class FilterConfig
    {
        public static void RegisterGlobalFilters(GlobalFilterCollection filters)
        {
            filters.Add(new HandleErrorAttribute
            {
                ExceptionType = typeof(System.Data.DataException),
                View = "Error"
            });
            filters.Add(new HandleErrorAttribute());
        }
    }
}
