using Microsoft.Ajax.Utilities;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Web;
using System.Web.Mvc;
using Workorder_web.Models;
using static Workorder_web.Models.Homepage;

namespace Workorder_web.Controllers
{

    public class HomeController : Controller
    {
        string[] Product_Name = new string[200];
        string[] Product_Month_sum = new string[200];
        //宣告欲儲存的已排列完的同一品項月排程表資料，已供圖表使用
        string[] Quantity_NoS = new string[200];
        //宣告儲存機種該月產出比例的陣列
        string[] Product_Month_proportion = new string[200];
        int Product_Month_all_output_count = 0;
        public ActionResult Index()
        {
            return RedirectToAction("Homepage");
        }
        //public ActionResult ProductionDailyReport_Print(string YearMonthDate)
        //{
        //    try
        //    {
        //        ViewBag.Message = "Your application description page.";
        //        ServiceReference1.Service1Client sc = new ServiceReference1.Service1Client();
        //        //string YearMonth = Year + Month;
        //        byte[] bytes = sc.ProductionDailyReport(YearMonthDate);
        //        Response.ContentType = "application/excel";
        //        Response.AddHeader("Content-disposition", "filename=output.xls");
        //        Response.OutputStream.Write(bytes, 0, bytes.Length);
        //        Response.OutputStream.Flush();
        //        Response.OutputStream.Close();
        //        Response.Flush();
        //        Response.Close();

        //        return View();
        //    }
        //    catch (Exception ex)
        //    {
        //        //網頁導到錯誤頁面
        //        return View("Error");
        //    }
        //}

        //public ActionResult Show_Produceplan_scheduleAction_Print(string year_month)
        //{
        //    try
        //    {
        //        ViewBag.Message = "Your application description page.";
        //        ServiceReference1.Service1Client sc = new ServiceReference1.Service1Client();
        //        //string YearMonth = Year + Month;
        //        byte[] bytes = sc.ProductionScheduleReport(year_month);
        //        Response.ContentType = "application/excel";
        //        Response.AddHeader("Content-disposition", "filename=output.xls");
        //        Response.OutputStream.Write(bytes, 0, bytes.Length);
        //        Response.OutputStream.Flush();
        //        Response.OutputStream.Close();
        //        Response.Flush();
        //        Response.Close();

        //        return View();
        //    }
        //    catch (Exception ex)
        //    {
        //        //網頁導到錯誤頁面
        //        return View("Error");
        //    }
        //}
        //public ActionResult Daily_schedule_data_Keyin_Show_Print(string YearMonthDate)
        //{
        //    try
        //    {
        //        ViewBag.Message = "Your application description page.";
        //        ServiceReference1.Service1Client sc = new ServiceReference1.Service1Client();
        //        byte[] bytes = sc.DailyProductionReport(YearMonthDate);

        //        Response.ContentType = "application/excel";
        //        Response.AddHeader("Content-disposition", "filename=output.xls");
        //        Response.OutputStream.Write(bytes, 0, bytes.Length);
        //        Response.OutputStream.Flush();
        //        Response.OutputStream.Close();
        //        Response.Flush();
        //        Response.Close();
        //        return View();
        //    }
        //    catch (Exception ex)
        //    {
        //        //網頁導到錯誤頁面
        //        return View("Error");
        //    }
        //}
        public ActionResult Homepage()
        {
            string myDateString = DateTime.Now.ToString("yyyyMM");
            Homepage Hp = new Homepage();
            ViewBag.data = Hp.Get_RequestsUploadChallenge();
            // 只用return View()會默認執行 _ViewStart.cshtml，因此會套用_layout模板
            //return View();
            //若用的是PartialView()會省略執行 _ViewStart.cshtml，因此不會套用_layout模板

            return PartialView();
        }
        public RedirectResult UpdateRequestsUploadChallenge(string RequestsUserID, string ChallengeName, string UploadPictureVideo1,string UploadPictureVideo2,
                                                            string ChallengeMissionExplan,string SpecialRequirement,DateTime UploadTime,string ApprovalStatus,string Topic,string Type)
        {
            if (Type != "")
            {
                Homepage Hp = new Homepage();
                if (ApprovalStatus == "通過")
                    Hp.UpdateRequestsUploadChallenge(RequestsUserID, ChallengeName, UploadPictureVideo1, UploadPictureVideo2, ChallengeMissionExplan, SpecialRequirement, UploadTime, "Y", Topic, Type);
                else
                    Hp.UpdateRequestsUploadChallenge(RequestsUserID, ChallengeName, UploadPictureVideo1, UploadPictureVideo2, ChallengeMissionExplan, SpecialRequirement, UploadTime, "N", Topic, Type);
                return new RedirectResult("Homepage", true);
            }
            else
            {
                TempData["shortMessage"] = "Error";
                return new RedirectResult("Homepage", true);
            }
        }
        //    public ActionResult Daily_schedule_data_Keyin_Show()
        //    {
        //        Homepage Hp = new Homepage();
        //        //ViewBag.data = Hp.GetMenuList();
        //        //ViewBag.ProductList = Hp.Getsp_ProductPainList();
        //        List<vw_ProductList> Customer_data = Hp.Getvw_ProductList();
        //        ViewBag.ErpPartNo = new SelectList(Customer_data, "Product_ID", "ERP_Part_No");
        //        ViewBag.ProductName = new SelectList(Customer_data, "Product_ID", "Product_Name");
        //        //ViewBag.OrderSerial = new SelectList(custom_data, "OrderSerial", "OrderSerial");
        //        ViewBag.ProductList_count = 0;

        //        return PartialView();
        //    }
        //    public ActionResult ProductionDailyReport_Show()
        //    {
        //        Homepage Hp = new Homepage();
        //        //ViewBag.data = Hp.GetMenuList();
        //        //ViewBag.ProductList = Hp.Getsp_ProductPainList();
        //        List<vw_ProductList> Customer_data = Hp.Getvw_ProductList();
        //        ViewBag.ErpPartNo = new SelectList(Customer_data, "Product_ID", "ERP_Part_No");
        //        ViewBag.ProductName = new SelectList(Customer_data, "Product_ID", "Product_Name");
        //        //ViewBag.OrderSerial = new SelectList(custom_data, "OrderSerial", "OrderSerial");
        //        ViewBag.ProductList_count = 0;

        //        return PartialView();
        //    }
        //    //輸入
        //    public ActionResult produceplan_schedule()
        //    {
        //        Homepage Hp = new Homepage();
        //        //List<Menus> custom_data = Hp.GetMenuList();
        //        //ViewBag.MenuID = new SelectList(custom_data, "MenuID", "MenuID");
        //        //ViewBag.Name = new SelectList(custom_data, "Name", "Name");
        //        //ViewBag.OrderSerial = new SelectList(custom_data, "OrderSerial", "OrderSerial");

        //        // 只用return View()會默認執行 _ViewStart.cshtml，因此會套用_layout模板
        //        //return View();
        //        //若用的是PartialView()會省略執行 _ViewStart.cshtml，因此不會套用_layout模板

        //        return PartialView();
        //    }




        //    //呈現年月份資料頁面 生產計劃排程表
        //    public ActionResult Show_Produceplan_scheduleAction() // put under the view
        //    {
        //        Homepage Hp = new Homepage();
        //        //ViewBag.data = Hp.GetMenuList();
        //        //ViewBag.ProductList = Hp.Getsp_ProductPainList();
        //        List<vw_ProductList> Customer_data = Hp.Getvw_ProductList();
        //        ViewBag.ErpPartNo = new SelectList(Customer_data, "Product_ID", "ERP_Part_No" );
        //        ViewBag.ProductName = new SelectList(Customer_data, "Product_ID", "Product_Name" );
        //        //ViewBag.OrderSerial = new SelectList(custom_data, "OrderSerial", "OrderSerial");
        //        ViewBag.ProductList_count = 0;
        //        return PartialView();
        //    }
        //    //取得ERP 對應的Product品名值，可下拉選單用
        //    public JsonResult GetProductList(string ERP_ID_select)
        //    {
        //        Homepage Hp = new Homepage();
        //        //取得對應的Product品名值
        //        List<vw_ProductList> Product_selectName = Hp.Dropdown_GetProductNameList(ERP_ID_select);
        //        //宣告儲存資料格式
        //        List<KeyValuePair<string, string>> items_Name = new List<KeyValuePair<string, string>>();


        //            var Products = Product_selectName;
        //            if (Products.Count() > 0)
        //            {
        //                foreach (var ProductName in Products)
        //                {
        //                //前面string 是Key 後面String是Value
        //                items_Name.Add(new KeyValuePair<string, string>(
        //                        ProductName.Product_Name.ToString(),
        //                        string.Format("{0}", ProductName.Product_Name)));
        //                }
        //            }

        //        return this.Json(items_Name, JsonRequestBehavior.AllowGet);
        //    }
        //    //取得Product品名 對應的ERP值，可下拉選單用
        //    public JsonResult GetERPList(string Product_ID_select)
        //    {
        //        Homepage Hp = new Homepage();
        //        //取得對應的ERP值
        //        List<vw_ProductList> Product_selectName = Hp.Dropdown_GetERPNameList(Product_ID_select);
        //        //宣告儲存資料格式
        //        List<KeyValuePair<string, string>> items_Name = new List<KeyValuePair<string, string>>();


        //        var Products = Product_selectName;
        //        if (Products.Count() > 0)
        //        {
        //            foreach (var ProductName in Products)
        //            { 
        //                //前面string 是Key 後面String是Value
        //                items_Name.Add(new KeyValuePair<string, string>(
        //                    ProductName.Product_Name.ToString(),
        //                    string.Format("{0}", ProductName.ERP_Part_No)));
        //            }
        //        }

        //        return this.Json(items_Name, JsonRequestBehavior.AllowGet);
        //    }

        //    //取得生產日報表工單號下拉選單對應的ERP 品名值，可下拉選單用  ***生產日報表下拉選單更改時專用***
        //    public JsonResult Get_sp_DailyProductionERPList(string Work_order_select ,string year_month_date)
        //    {
        //        Homepage Hp = new Homepage();
        //        //取得對應的Product品名值
        //        List<sp_DailyProductionList_Result> ERP_selectName = Hp.Dropdown_sp_DailyProduction_ERPList(Work_order_select, year_month_date);
        //        //宣告儲存資料格式
        //        List<KeyValuePair<string, string>> items_Name = new List<KeyValuePair<string, string>>();


        //        var Products = ERP_selectName;
        //        if (Products.Count() > 0)
        //        {
        //            foreach (var ProductName in Products)
        //            {
        //                //前面string 是Key 後面String是Value
        //                items_Name.Add(new KeyValuePair<string, string>(
        //                        ProductName.Work_order_volume.ToString(),
        //                        string.Format("{0}", ProductName.ERP_Part_No)));
        //            }
        //        }

        //        return this.Json(items_Name, JsonRequestBehavior.AllowGet);
        //    }

        //    //取得生產日報表ERP下拉選單對應的工單號品名值，可下拉選單用  ***生產日報表下拉選單更改時專用***
        //    public JsonResult Get_sp_DailyProductionWork_Order_List(string Work_order_select, string year_month_date)
        //    {
        //        Homepage Hp = new Homepage();
        //        //取得對應的Product品名值
        //        List<sp_DailyProductionList_Result> ERP_selectName = Hp.Dropdown_sp_DailyProduction_Work_Order_List(Work_order_select, year_month_date);
        //        //宣告儲存資料格式
        //        List<KeyValuePair<string, string>> items_Name = new List<KeyValuePair<string, string>>();


        //        var Products = ERP_selectName;
        //        if (Products.Count() > 0)
        //        {
        //            foreach (var ProductName in Products)
        //            {
        //                //前面string 是Key 後面String是Value
        //                items_Name.Add(new KeyValuePair<string, string>(
        //                        ProductName.Work_order_volume.ToString(),
        //                        string.Format("{0}", ProductName.Work_Order)));
        //            }
        //        }

        //        return this.Json(items_Name, JsonRequestBehavior.AllowGet);
        //    }

        //    //計畫排程表取得資料庫sp_ProductPainList_Result資料表 對應使用者取的年月資料所有資料
        //    public JsonResult GetYeatMonthProductList(string Year_Month)
        //    {
        //        Homepage Hp = new Homepage();
        //        //取得年月資料
        //        List<sp_ProductPainList_Result> Product_List = Hp.GetYearMonthProduct_List(Year_Month);
        //        //宣告儲存資料格式
        //        List<KeyValuePair<string, string>> items_Name = new List<KeyValuePair<string, string>>();

        //        //若傳來不是空的 or 空白字串
        //        if (!string.IsNullOrWhiteSpace(Year_Month))
        //        {
        //            var Products = Product_List;
        //            if (Products.Count() > 0)
        //            {
        //                foreach (var ProductName in Products)
        //                {
        //                    //前面string 是Key 後面String是Value
        //                    items_Name.Add(new KeyValuePair<string, string>(
        //                        ProductName.Product_Name.ToString(),
        //                        string.Format("{0} ~{1} !{2:yyyy-MM-dd} ${3} #{4} &{5} %{6} /{7}", ProductName.Product_Name, ProductName.ERP_Part_No, ProductName.date, ProductName.Quantity, ProductName.Product_ID,ProductName.vision, ProductName.ASSEMBLY_COUNT, ProductName.Production_Schedule_ID)));
        //                }
        //            }
        //        }
        //        //string jsonData = JsonConvert.SerializeObject(items_Name);
        //        //回傳資料，一要要加JsonRequestBehavior.AllowGet，可能是安全性問題
        //        return this.Json(items_Name, JsonRequestBehavior.AllowGet);
        //    }

        //    //計畫排程表取得資料庫vw_ProductionDailyReportVision對應使用者選取的年月資料版本
        //    public JsonResult GetYeatMonthvw_ProductionDailyReportVisionList(string Year_Month)
        //    {
        //        Homepage Hp = new Homepage();
        //        //取得年月資料
        //        List<sp_DailyProductionList_Result> Product_List = Hp.GetYeatMonthProduct_Vision_List(Year_Month);
        //        //宣告儲存資料格式
        //        List<KeyValuePair<string, string>> items_Name = new List<KeyValuePair<string, string>>();

        //        //若傳來不是空的 or 空白字串
        //        if (!string.IsNullOrWhiteSpace(Year_Month))
        //        {
        //            var Products = Product_List;
        //            if (Products.Count() > 0)
        //            {
        //                foreach (var ProductName in Products)
        //                {
        //                    //前面string 是Key 後面String是Value
        //                    items_Name.Add(new KeyValuePair<string, string>(
        //                        ProductName.Product_Name.ToString(),
        //                        string.Format("{0}", ProductName.vision)));
        //                }
        //            }
        //        }

        //        //回傳資料，一要要加JsonRequestBehavior.AllowGet，可能是安全性問題
        //        return this.Json(items_Name, JsonRequestBehavior.AllowGet);
        //    }
        //    //計畫表上傳資料庫函式
        //    public JsonResult Upload_tabledata_to_database(string Date_send, string Quantity_send, string ProductID_send,string Vision_send)
        //    {
        //        Homepage Hp = new Homepage();
        //        Hp.CreateProductionplanningscheduleData(Date_send, Quantity_send, ProductID_send, Vision_send);
        //        return this.Json(Date_send, JsonRequestBehavior.AllowGet);
        //    }

        //    //日生產排程上傳資料庫函式
        //    public JsonResult Upload_tabledata_to_database_DailyProductionSchedule(
        //        string Floor_send, 
        //        string Line_send, 
        //        string Leader_send, 
        //        string Target_Capacity_send,
        //        string Actual_Capacity_send,
        //        string People_send,
        //        string Planning_time_send,
        //        string Cumulative_time_send,
        //        string Work_order_volume_send,
        //        string Work_order_send,
        //        string Note_send,
        //        string ProductionplanningID_send,
        //        string Vision_send
        //        )
        //    {
        //        Homepage Hp = new Homepage();
        //        Hp.CreateDailyProductionScheduleData(
        //            Floor_send,
        //            Line_send, 
        //            Leader_send, 
        //            Target_Capacity_send,
        //            Actual_Capacity_send, 
        //            People_send, 
        //            Planning_time_send,
        //            Cumulative_time_send,
        //            Work_order_volume_send,
        //            Work_order_send,
        //            Note_send,
        //            ProductionplanningID_send,
        //            Vision_send
        //            );
        //        return this.Json(Line_send, JsonRequestBehavior.AllowGet);
        //    }

        //    //生產日報表資料上傳資料庫函式
        //    public JsonResult Upload_tabledata_to_database_ProductionDailyReportList(
        //        string Work_order_send,
        //        string Model_or_Part_No_send,
        //        string Work_order_volume_send,
        //        string Semi_finished_products_send,
        //        string Finished_products_send,
        //        string People_send,
        //        string Working_hours_send,
        //        string Working_hours_total_send,
        //        string Standard_capacity_send,
        //        string Poor_incoming_send,
        //        string Poor_productivity_send,
        //        string Poor_operation_send,
        //        string Capacity_achievement_rate_send,
        //        string productivity,
        //        string Ask_leave,
        //        string Overtime_hours,
        //        string Start_period,
        //        string End_period,
        //        string effectiveness_H,
        //        string createDate,
        //        string Vision_send
        //        )
        //    {
        //        Homepage Hp = new Homepage();
        //        Hp.CreateProductionDailyReportListData(
        //            Work_order_send,
        //            Model_or_Part_No_send,
        //            Work_order_volume_send,
        //            Semi_finished_products_send,
        //            Finished_products_send,
        //            People_send,
        //            Working_hours_send,
        //            Working_hours_total_send,
        //            Standard_capacity_send,
        //            Poor_incoming_send,
        //            Poor_productivity_send,
        //            Poor_operation_send,
        //            Capacity_achievement_rate_send,
        //            productivity,
        //            Ask_leave,
        //            Overtime_hours,
        //            Start_period,
        //            End_period,
        //            effectiveness_H,
        //            createDate,
        //            Vision_send
        //            );
        //        return this.Json(Work_order_send, JsonRequestBehavior.AllowGet);
        //    }
        //    //生產日報表取得資料庫內對應使用者取的年月日資料所有資料
        //    public JsonResult GetYeatMonthDate_ProductionDailyReportList(string Year_Month_Date)
        //    {
        //        Homepage Hp = new Homepage();
        //        //取得年月資料
        //        List<sp_DailyProductionList_Result> Product_List = Hp.GetYeatMonthDate_ProductionDailyReport_List(Year_Month_Date);
        //        //宣告儲存資料格式
        //        List<KeyValuePair<string, string>> items_Name = new List<KeyValuePair<string, string>>();

        //        //若傳來不是空的 or 空白字串
        //        if (!string.IsNullOrWhiteSpace(Year_Month_Date))
        //        {
        //            var Products = Product_List;
        //            if (Products.Count() > 0)
        //            {
        //                foreach (var ProductName in Products)
        //                {
        //                    //前面string 是Key 後面String是Value
        //                    items_Name.Add(new KeyValuePair<string, string>(
        //                        ProductName.Product_Name.ToString(),
        //                        string.Format("{0} ~{1} !{2:yyyy-MM-dd} ${3} #{4} &{5} %{6} /{7} ]{8} ^{9} *{10} <{11} >{12} ?{13} |{14} +{15}", 
        //                        ProductName.Product_Name, 
        //                        ProductName.ERP_Part_No, 
        //                        ProductName.Date, 
        //                        ProductName.floor, 
        //                        ProductName.Line_type, 
        //                        ProductName.vision, 
        //                        ProductName.Principal, 
        //                        ProductName.Target_capacity, 
        //                        ProductName.Actual_capacity, 
        //                        ProductName.People, 
        //                        ProductName.Planning_time, 
        //                        ProductName.Cumulative_time, 
        //                        ProductName.Work_order_volume, 
        //                        ProductName.Arrange_date, 
        //                        ProductName.note, 
        //                        ProductName.Work_Order)));
        //                }
        //            }
        //        }

        //        //回傳資料，一要要加JsonRequestBehavior.AllowGet，可能是安全性問題
        //        return this.Json(items_Name, JsonRequestBehavior.AllowGet);
        //    }

        //    //從sp_getOrderCapacity 資料表獲取該日各工單實際產線情況
        //    public JsonResult GetOrderCapacity_sp_getOrderCapacityList(string Year_Month_Date)
        //    {
        //        Homepage Hp = new Homepage();
        //        //取得年月資料
        //        List<sp_getOrderCapacity_Result> Order_situation_List = Hp.GetOrderCapacity_sp_getOrderCapacity_List(Year_Month_Date);
        //        //宣告儲存資料格式
        //        List<KeyValuePair<string, string>> items_Name = new List<KeyValuePair<string, string>>();

        //        //若傳來不是空的 or 空白字串
        //        if (!string.IsNullOrWhiteSpace(Year_Month_Date))
        //        {
        //            var Order = Order_situation_List;
        //            if (Order.Count() > 0)
        //            {
        //                foreach (var Order_data in Order)
        //                {
        //                    //前面string 是Key 後面String是Value
        //                    items_Name.Add(new KeyValuePair<string, string>(
        //                        Order_data.Order_No.ToString(),
        //                        string.Format("{0} ~{1}",
        //                        Order_data.PRODUCT_CAPACITY,
        //                        Order_data.REAL_CAPACITY)));
        //                }
        //            }
        //        }

        //        //回傳資料，一要要加JsonRequestBehavior.AllowGet，可能是安全性問題
        //        return this.Json(items_Name, JsonRequestBehavior.AllowGet);
        //    }
        //    //生產日報表取得資料庫的ProductionDailyReport資料表內工單號已有資料
        //    public JsonResult Get_sp_ProductionDailyReportList_exist_dataList(string Year_Month_Date)
        //    {
        //        Homepage Hp = new Homepage();
        //        //取得年月資料
        //        List<sp_ProductionDailyReportList_Result> Product_List = Hp.Get_sp_ProductionDailyReportList_exist_data_List(Year_Month_Date);
        //        //宣告儲存資料格式
        //        List<KeyValuePair<string, string>> items_Name = new List<KeyValuePair<string, string>>();

        //        //若傳來不是空的 or 空白字串

        //            var Products = Product_List;
        //            if (Products.Count() > 0)
        //            {
        //                foreach (var ProductName in Products)
        //                {
        //                    //前面string 是Key 後面String是Value
        //                    items_Name.Add(new KeyValuePair<string, string>(
        //                        ProductName.Work_Order_Number.ToString(),
        //                        string.Format("{0} ~{1} !{2} ${3} #{4} &{5} %{6} /{7} ]{8} ^{9} *{10} <{11} >{12} ?{13} |{14} +{15} 結{16} 數{17} 版{18}",
        //                        ProductName.Model_or_Part_No,
        //                        ProductName.Allocation,
        //                        ProductName.Semi_finished_products,
        //                        ProductName.Finished_products,
        //                        ProductName.People,
        //                        ProductName.Working_hours,
        //                        ProductName.Working_hours_total,
        //                        ProductName.Standard_capacity,
        //                        ProductName.Poor_incoming,
        //                        ProductName.Poor_operation,
        //                        ProductName.Poor_productivity,
        //                        ProductName.Capacity_achievement_rate,
        //                        ProductName.productivity,
        //                        ProductName.Ask_leave,
        //                        ProductName.Overtime_hours,
        //                        ProductName.Start_period,
        //                        ProductName.End_period,
        //                        ProductName.effectiveness_H,
        //                        ProductName.vision
        //                        )));
        //                }
        //            }


        //        //回傳資料，一要要加JsonRequestBehavior.AllowGet，可能是安全性問題
        //        return this.Json(items_Name, JsonRequestBehavior.AllowGet);
        //    }
        //    //取得產品相關訊息
        //    public JsonResult Get_vw_ProductList_data_List()
        //    {
        //        Homepage Hp = new Homepage();
        //        //取得年月資料
        //        List < vw_ProductList > vw_Product_List_data = Hp.Getvw_ProductList();
        //        //宣告儲存資料格式
        //        List<KeyValuePair<string, string>> items_Name = new List<KeyValuePair<string, string>>();

        //        //若傳來不是空的 or 空白字串

        //        var Products = vw_Product_List_data;
        //        if (Products.Count() > 0)
        //        {
        //            foreach (var ProductName in Products)
        //            {
        //                //前面string 是Key 後面String是Value
        //                items_Name.Add(new KeyValuePair<string, string>(
        //                    ProductName.Client_Name.ToString(),
        //                    string.Format("{0} ~{1} !{2} ${3} #{4}",
        //                    ProductName.ERP_Part_No,
        //                    ProductName.Product_Name,
        //                    ProductName.ASSEMBLY_TIME,
        //                    ProductName.ASSEMBLY_COUNT, 
        //                    ProductName.Product_ID
        //                    )));
        //            }
        //        }


        //        //回傳資料，一要要加JsonRequestBehavior.AllowGet，可能是安全性問題
        //        return this.Json(items_Name, JsonRequestBehavior.AllowGet);
        //    }
        //    //取得產品當月銷售價錢
        //    public JsonResult Get_Product_output_price(string Year_Month_Date)
        //    {

        //        string Product_data="";
        //        Homepage Hp = new Homepage();
        //        //設定向後端抓取資料的時間，若超過將會傳送指定文字給前端(透過這段文字可以觸發特定事件)
        //        //TimeSpan ts = TimeSpan.FromMilliseconds(5000);
        //        //宣告儲存資料格式
        //        List<KeyValuePair<string, string>> items_Name = new List<KeyValuePair<string, string>>();
        //        List<sp_AutoGetERPPartPrice_Result> Product_Price= Hp.GetPrice(Year_Month_Date);

        //        foreach (var PrPr in Product_Price)
        //        {
        //            items_Name.Add(new KeyValuePair<string, string>(
        //                    PrPr.part,
        //                    (PrPr.price).ToString()
        //                    ));
        //        }


        //        return this.Json(items_Name, JsonRequestBehavior.AllowGet);
        //        //Task t = Task.Run(() =>
        //        //{
        //        //    //連接伺服器上的Webservice，以此獲得銷售額data
        //        //    ServiceReference1.Service1Client sc = new ServiceReference1.Service1Client();
        //        //    //儲存銷售額的值
        //        //    Product_data = sc.GetProductPrice("GT", Erp_Name);
        //        //    //Thread.Sleep(6000);

        //        //    //JObject json = JObject.Parse(Product_data);


        //        //    //前面string 是Key 後面String是Value
        //        //    items_Name.Add(new KeyValuePair<string, string>(
        //        //            Product_name,
        //        //            Product_data
        //        //            ));
        //        //});
        //        ////回傳資料，一要要加JsonRequestBehavior.AllowGet，可能是安全性問題
        //        //// return this.Json(items_Name, JsonRequestBehavior.AllowGet);
        //        ////反向(若Task在指定秒數內做完=True)
        //        //if (!t.Wait(ts))
        //        //{
        //        //    Console.WriteLine("抓取資料異常");
        //        //    items_Name.Add(new KeyValuePair<string, string>(
        //        //           "Error",
        //        //           "Error"
        //        //           ));
        //        //    return this.Json(items_Name, JsonRequestBehavior.AllowGet);
        //        //}
        //        ////若Task在指定秒數內做完=True ，就會執行下面
        //        //else
        //        //{ 
        //        //    return this.Json(items_Name, JsonRequestBehavior.AllowGet); 
        //        //}

        //    }
        //    // 計算各機種月分配率和 設定預估該月銷售總額與機種配比圖表顏色參數
        //    public JsonResult calculate_Product_Month_proportion(string Product_Name, string Quantity_NoS)
        //    {
        //        char[] Product_Month_Name;
        //        string[] Product_Name_Array;
        //        string[] Quantity_NoS_Array;
        //        //string[] Product_Name_Array_;
        //        string[] Product_Month_proportion;
        //        float Product_Month_output_count = 0;
        //        //宣告儲存各機種月分配率圖表該月機種名稱
        //        string[] Product_Month_sum;
        //        //隨便宣告 先給予陣列值
        //        var dad = "dada,";
        //        Product_Month_sum = dad.Split(',');
        //        Product_Month_proportion = dad.Split(',');

        //        Product_Name = Product_Name.Replace("\r\n", "");
        //        Product_Name = Product_Name.Replace(" ", "");
        //        Product_Name = Product_Name.Replace("\"", "");
        //        Product_Name = Product_Name.Replace("[],", "");
        //        Product_Name = Product_Name.Replace(",[]", "");
        //        string Product_Name_ = Product_Name;
        //        //刪除多的字元
        //        Product_Name_ = Product_Name_.Remove(0, 1);
        //        Product_Name_ = Product_Name_.Substring(0, Product_Name_.Length - 1);

        //        Quantity_NoS = Quantity_NoS.Replace("\r\n", "");
        //        Quantity_NoS = Quantity_NoS.Replace(" ", "");
        //        Quantity_NoS = Quantity_NoS.Replace("\"", "");
        //        Quantity_NoS = Quantity_NoS.Replace(",[", ".[");
        //        string Quantity_NoS_ = Quantity_NoS;
        //        Quantity_NoS_ = Quantity_NoS_.Remove(0, 1);
        //        Quantity_NoS_ = Quantity_NoS_.Substring(0, Quantity_NoS_.Length - 1);

        //        //拆解成陣列
        //        Product_Name_Array = Product_Name_.Split(',');
        //        Quantity_NoS_Array = Quantity_NoS_.Split('.');

        //        //計算單一機種該月預計產出總數和該機種佔該月製作產品的總量為多少
        //        for (var Month_Product_count = 0; Month_Product_count < Product_Name_Array.Length; Month_Product_count++)
        //        {
        //            Product_Month_output_count = 0;
        //            //如果該筆陣列沒有存在值就跳過
        //            if (Product_Name_Array[Month_Product_count] == "")
        //            {
        //                continue;
        //            }
        //            //有的話計算該筆機種的該月預計產出總和
        //            else
        //            {
        //                //儲存該月機種名稱到一個陣列裡面
        //                //List<string> list = new List<string>(Product_Name_Array.ToList());
        //                //list.Add(Product_Name_Array[Month_Product_count]);
        //                //Product_Name_Array= list.ToArray();
        //                //Product_Month_Name.push(Product_Name_Array[Month_Product_count]);
        //                //計算單機機種該月預計出貨總數量
        //                //換成字元 然後相加出總量
        //                Product_Month_Name = Quantity_NoS_Array[Month_Product_count].ToCharArray();
        //                for (var oo = 0; oo < Product_Month_Name.Length; oo++)
        //                {
        //                    Product_Month_output_count += Convert.ToInt32(Product_Month_Name[oo]);
        //                }
        //                //Product_Month_output_count += Convert.ToInt32(Quantity_NoS_Array[Month_Product_count][date_count]);


        //                //計算全部機種量的總和
        //                Product_Month_all_output_count += Convert.ToInt32(Product_Month_output_count);
        //                List<string> list2 = new List<string>(Product_Month_sum.ToList());
        //                if(Month_Product_count==0) list2.Clear();
        //                list2.Add(Product_Month_output_count.ToString());
        //                Product_Month_sum = list2.ToArray();

        //                //Product_Month_sum.push(Product_Month_output_count);

        //            }


        //        }
        //        //運算單一機種該月分配比例
        //        for (var proportion_count = 0; proportion_count < Product_Name_Array.Length; proportion_count++)
        //        {
        //            Product_Month_output_count = float.Parse((( float.Parse(Product_Month_sum[proportion_count]) / Product_Month_all_output_count ) * 100).ToString("f2"));

        //            //儲存比例
        //            List<string> list3 = new List<string>(Product_Month_proportion.ToList());
        //            if (proportion_count == 0) list3.Clear();
        //            list3.Add(Product_Month_output_count.ToString());
        //            Product_Month_proportion = list3.ToArray();
        //            //Product_Month_proportion.push(Product_Month_output_count);
        //            //儲存顏色
        //            //var color_chart = rgba_random(0.5);
        //            //Product_Pie_color.push(color_chart);
        //        }
        //        List<KeyValuePair<string, string>> items_Name = new List<KeyValuePair<string, string>>();
        //        if (Product_Month_proportion.Count() > 0)
        //        {
        //            for (var count = 0; count < Product_Month_proportion.Length; count++)
        //            {
        //                //前面string 是Key 後面String是Value
        //                items_Name.Add(new KeyValuePair<string, string>(
        //                    Product_Month_proportion[count].ToString(),
        //                    Product_Month_sum[count].ToString()));
        //            }
        //        }
        //        return this.Json(items_Name, JsonRequestBehavior.AllowGet);
        //    }
    }
}