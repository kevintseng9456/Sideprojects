using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.ComponentModel.DataAnnotations;

namespace Workorder_web.Models
{
    public class Homepage
    {
    //    public string MenuID { get; set; }
    //    public string Name { get; set; }
    //    public string Controller { get; set; }
    //    public string Action { get; set; }
    //    public string Url { get; set; }
    //    public string Description { get; set; }
    //    public Nullable<int> ParentID { get; set; }
    //    public string Statuse { get; set; }
    //    public string RouteValues { get; set; }
    //    public string OrderSerial { get; set; }

    //    [DataType(DataType.Date)]
    //    public DateTime date_chioce { get; set; }

    //    public partial class ProductList_par
    //    {
    //        public string Client_Name { get; set; }
    //        public string ERP_Part_No { get; set; }
    //        public string Product_Name { get; set; }
    //        public Nullable<double> ASSEMBLY_TIME { get; set; }
    //        public Nullable<double> ASSEMBLY_COUNT { get; set; }
    //    }
    //    public partial class vw_ProductPainList_parameter
    //    {
    //        public string Product_Name { get; set; }
    //        public string ERP_Part_No { get; set; }
    //        public Nullable<System.DateTime> Date { get; set; }
    //        public Nullable<int> Quantity { get; set; }
    //    }
    //    public partial class Productionplanningschedule_parameter
    //    {
    //        public int Production_Schedule_ID { get; set; }
    //        public int Product_ID { get; set; }
    //        public Nullable<System.DateTime> Date { get; set; }
    //        public Nullable<int> Quantity { get; set; }
    //        public Nullable<System.DateTime> CreateDate { get; set; }
    //    }

        
    //    public List<sp_ProductPainList_Result> Getsp_ProductPainList(string Year_Month)
    //    {
    //        List<sp_ProductPainList_Result> List = new List<sp_ProductPainList_Result>();
    //        SyncGTEntities db = new SyncGTEntities();
    //        List = db.sp_ProductPainList(Year_Month).Where(x => (x.ERP_Part_No != "NULL")).ToList();
    //        return List;
    //    }
    //    //取得檢視表sp_GetOrderCount的工單量資料
        public List<GetRequestsUploadChallenge_Result> Get_RequestsUploadChallenge()

        {
            
            List<GetRequestsUploadChallenge_Result> List = new List<GetRequestsUploadChallenge_Result>();
            APPSolutionsEntities db = new APPSolutionsEntities();
            List = db.GetRequestsUploadChallenge().Where(x => (x.RequestsUserID != "NULL")).ToList();
            return List;
        }
        public void UpdateRequestsUploadChallenge(string RequestsUserID, string ChallengeName, string UploadPictureVideo1, string UploadPictureVideo2,
                                                  string ChallengeMissionExplan, string SpecialRequirement, DateTime UploadTime, string ApprovalStatus, string Topic, string Type)
        {
            if (ApprovalStatus == "Y")
            {
                APPSolutionsEntities db = new APPSolutionsEntities();
                List<UpdateRequestsUploadChallenge_Result> List = new List<UpdateRequestsUploadChallenge_Result>();
                //更改審核紀錄
                List = db.UpdateRequestsUploadChallenge(RequestsUserID, ChallengeName, UploadPictureVideo1, UploadPictureVideo2, ChallengeMissionExplan,
                                                SpecialRequirement, UploadTime, ApprovalStatus).ToList();
                //新增任務到ChallengeName資料表
                db.UploadNewChallenge(Topic, Type, ChallengeName);
                //修改儲存，若沒有這個可能無法如期更改資料表內容
                //db.SaveChanges();
            }
            else
            {
                APPSolutionsEntities db = new APPSolutionsEntities();
                List<UpdateRequestsUploadChallenge_Result> List = new List<UpdateRequestsUploadChallenge_Result>();
                List = db.UpdateRequestsUploadChallenge(RequestsUserID, ChallengeName, UploadPictureVideo1, UploadPictureVideo2, ChallengeMissionExplan,
                                                SpecialRequirement, UploadTime, ApprovalStatus).ToList();
                //修改儲存，若沒有這個可能無法如期更改資料表內容
                //db.SaveChanges();
            }
        }
    //    //取得Product產品List
    //    public List<vw_ProductList> Getvw_ProductList()

        //    {
        //        List<vw_ProductList> List = new List<vw_ProductList>();
        //        SyncGTEntities db = new SyncGTEntities();
        //        List = db.vw_ProductList.Where(x => (x.ERP_Part_No !="NULL")).ToList();
        //        return List;
        //    }


        //    //計畫排程表取得資料庫sp_ProductPainList_Result 對應使用者取的年月資料所有資料
        //    public List<sp_ProductPainList_Result> GetYearMonthProduct_List(string ERP_select)
        //    {
        //        List<sp_ProductPainList_Result> List = new List<sp_ProductPainList_Result>();
        //        SyncGTEntities db = new SyncGTEntities();
        //        List = db.sp_ProductPainList(ERP_select).Where(x => x.ERP_Part_No !="").ToList();
        //        return List;
        //    }

        //    //計畫排程表取得資料庫 對應使用者取的年月資料所有資料
        //    public List<sp_DailyProductionList_Result> GetYeatMonthDate_ProductionDailyReport_List(string Year_Month_Date)
        //    {
        //        List<sp_DailyProductionList_Result> List = new List<sp_DailyProductionList_Result>();
        //        SyncGTEntities db = new SyncGTEntities();
        //        List = db.sp_DailyProductionList(Year_Month_Date).Where(x => x.ERP_Part_No != "").ToList();
        //        return List;
        //    }
        //    //取得網頁系統首頁-->工單要顯示的效率
        //    public List<sp_getOrderCapacity_Result> GetOrderCapacity_sp_getOrderCapacity_List(string Year_Month_Date)
        //    {
        //        List<sp_getOrderCapacity_Result> List = new List<sp_getOrderCapacity_Result>();
        //        SyncGTEntities db = new SyncGTEntities();
        //        List = db.sp_getOrderCapacity(Year_Month_Date).Where(x => x.Order_No != "").ToList();
        //        return List;
        //    }
        //    //計畫排程表取得資料庫sp_DailyProductionList 對應使用者選取的年月資料版本
        //    public List<sp_DailyProductionList_Result> GetYeatMonthProduct_Vision_List(string ERP_select)
        //    {
        //        List<sp_DailyProductionList_Result> List = new List<sp_DailyProductionList_Result>();
        //        SyncGTEntities db = new SyncGTEntities();
        //        List = db.sp_DailyProductionList(ERP_select).Where(x => x.Product_Name != "").ToList();
        //        return List;
        //    }
        //    //計畫排程表取得資料庫的資料表sp_ProductionDailyReportList先前工單號已存有的資料
        //    public List<sp_ProductionDailyReportList_Result> Get_sp_ProductionDailyReportList_exist_data_List(string Year_Month_Date)
        //    {
        //        List<sp_ProductionDailyReportList_Result> List = new List<sp_ProductionDailyReportList_Result>();
        //        SyncGTEntities db = new SyncGTEntities();
        //        List = db.sp_ProductionDailyReportList(Year_Month_Date).Where(x => x.Work_Order_Number != "").ToList();
        //        return List;
        //    }
        //    //當選擇ERP下拉選單時獲取對應的Product值
        //    public List<vw_ProductList> Dropdown_GetProductNameList(string ERP_ID_select)
        //    {
        //        List<vw_ProductList> List = new List<vw_ProductList>();
        //        SyncGTEntities db = new SyncGTEntities();
        //        List = db.vw_ProductList.Where(x => x.Product_ID == ERP_ID_select).ToList();
        //        return List;
        //    }

        //    //當選擇工單號下拉選單時獲取對應的ERP值 生產日報表專用
        //    public List<sp_DailyProductionList_Result> Dropdown_sp_DailyProduction_ERPList(string Work_order_select, string year_month_date)
        //    {
        //        List<sp_DailyProductionList_Result> List = new List<sp_DailyProductionList_Result>();
        //        SyncGTEntities db = new SyncGTEntities();
        //        List = db.sp_DailyProductionList(year_month_date).Where(x => x.Work_Order == Work_order_select).ToList();
        //        return List;
        //    }
        //    //當選擇工單號下拉選單時獲取對應的ERP值 生產日報表專用
        //    public List<sp_DailyProductionList_Result> Dropdown_sp_DailyProduction_Work_Order_List(string ERP_select, string year_month_date)
        //    {
        //        List<sp_DailyProductionList_Result> List = new List<sp_DailyProductionList_Result>();
        //        SyncGTEntities db = new SyncGTEntities();
        //        List = db.sp_DailyProductionList(year_month_date).Where(x => x.ERP_Part_No == ERP_select).ToList();
        //        return List;
        //    }

        //    //當選擇Product下拉選單時獲取對應的ERP值
        //    public List<vw_ProductList> Dropdown_GetERPNameList(string Product_ID_select)
        //    {
        //        List<vw_ProductList> List = new List<vw_ProductList>();
        //        SyncGTEntities db = new SyncGTEntities();
        //        List = db.vw_ProductList.Where(x => x.Product_ID == Product_ID_select).ToList();
        //        return List;
        //    }
        //    //上傳Table內容至資料庫的Productionplanningschedule上面
        //    public void CreateProductionplanningscheduleData(string date_data,string Qnautity_data,string Product_ID_data,string Vision_data)
        //    {
        //        string time_data="";
        //        int Vision_math=0;
        //        Vision_math = int.Parse(Vision_data);
        //        //更新版本
        //        Vision_math = Vision_math + 1;

        //        time_data = DateTime.Now.ToString("yyyy-MM-dd") +" "+ DateTime.Now.TimeOfDay;
        //        //REMAPING THE PROJECTID
        //        SyncGTEntities db = new SyncGTEntities();
        //        Productionplanningschedule data = new Productionplanningschedule();

        //        //string myDateString = data_load.Date.ToString("yyyy-MM-dd");

        //        data.Product_ID = Product_ID_data;
        //        data.Date = Convert.ToDateTime(date_data);
        //        data.Quantity = int.Parse(Qnautity_data);
        //        data.CreateDate = Convert.ToDateTime(time_data);
        //        data.Vision = Vision_math;
        //        //資料表加入data
        //        db.Productionplanningschedule.Add(data);
        //        //修改儲存，若沒有這個可能無法如期更改資料表內容
        //        db.SaveChanges();

        //  }

        //    //上傳Table內容至資料庫的DailyProductionSchedule上面
        //    public void CreateDailyProductionScheduleData(
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
        //        string time_data = "";
        //        int Vision_math = 0;
        //        //若資料庫沒有此筆資料時 設為新的Vision從"0"開始算起
        //        if (Vision_send == null)
        //        {
        //            Vision_send = "0";
        //        }
        //        //Vision_math = int.Parse(Vision_data);
        //        ////更新版本
        //        //Vision_math = Vision_math + 1;

        //        time_data = DateTime.Now.ToString("yyyy-MM-dd") + " " + DateTime.Now.TimeOfDay;
        //        ////REMAPING THE PROJECTID
        //        SyncGTEntities db = new SyncGTEntities();
        //        DailyProductionSchedule data = new DailyProductionSchedule();

        //        string myDateString = DateTime.Now.ToString("yyyy-MM-dd");

        //        data.ProductionplanningID = int.Parse(ProductionplanningID_send);
        //        data.Target_capacity = Double.Parse(Target_Capacity_send);
        //        data.Actual_capacity = Double.Parse(Actual_Capacity_send);
        //        data.People = double.Parse(People_send);
        //        data.Planning_time= Double.Parse(Planning_time_send);
        //        data.Cumulative_time = Double.Parse(Cumulative_time_send);
        //        data.Work_order_volume = int.Parse(Work_order_volume_send);
        //        data.Work_Order = Work_order_send;
        //        data.floor = Floor_send;
        //        data.Line_type = Line_send;
        //        data.Principal = Leader_send;
        //        data.CreateDate = Convert.ToDateTime(myDateString);
        //        data.vision = int.Parse(Vision_send)+1;

        //        data.note = Note_send;
        //        //data.CreateDate = Convert.ToDateTime(time_data);
        //        //data.Vision = Vision_math;
        //        ////資料表加入data
        //        db.DailyProductionSchedule.Add(data);
        //        ////修改儲存，若沒有這個可能無法如期更改資料表內容
        //        db.SaveChanges();

        //    }
        //    //上傳Table內容至資料庫的ProductionDailyReportList上面
        //    public void CreateProductionDailyReportListData(
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
        //        string productivity_send,
        //        string Ask_leave_send,
        //        string Overtime_hours_send,
        //        string Start_period_send,
        //        string End_period_send,
        //        string effectiveness_H,
        //        string createDate_send,
        //        string Vision_send
        //        )
        //    {
        //        string time_data = "";
        //        //int Vision_math = 0;

        //        //Vision_math = int.Parse(Vision_data);
        //        ////更新版本
        //        //Vision_math = Vision_math + 1;

        //        //time_data = DateTime.Now.ToString("yyyy-MM-dd") + " " + DateTime.Now.TimeOfDay;
        //        ////REMAPING THE PROJECTID
        //        SyncGTEntities db = new SyncGTEntities();

        //        ProductionDailyReport data = new ProductionDailyReport();



        //        //string myDateString = DateTime.Now.ToString("yyyy-MM-dd");
        //        //判斷資料庫已存在此筆工單號，因此修改此工單號資訊

        //            if (Work_order_send != "") data.Work_Order_Number = Work_order_send;
        //            if (Model_or_Part_No_send != "") data.Model_or_Part_No = Model_or_Part_No_send;
        //            if (Work_order_volume_send != "") data.Allocation = Double.Parse(Work_order_volume_send);
        //            if (Semi_finished_products_send != "") data.Semi_finished_products = Double.Parse(Semi_finished_products_send);
        //            if (Finished_products_send != "") data.Finished_products = Double.Parse(Finished_products_send);
        //            if (People_send != "") data.People = Double.Parse(People_send);
        //            if (Working_hours_send != "") data.Working_hours = Double.Parse(Working_hours_send);
        //            if (Working_hours_total_send != "") data.Working_hours_total = Double.Parse(Working_hours_total_send);
        //            if (Standard_capacity_send != "") data.Standard_capacity = Double.Parse(Standard_capacity_send);
        //            if (Poor_incoming_send != "") data.Poor_incoming = Double.Parse(Poor_incoming_send);
        //            if (Poor_productivity_send != "") data.Poor_productivity = Double.Parse(Poor_productivity_send);
        //            if (Poor_operation_send != "") data.Poor_operation = Double.Parse(Poor_operation_send);
        //            if (Capacity_achievement_rate_send != "") data.Capacity_achievement_rate = Double.Parse(Capacity_achievement_rate_send);
        //            if (productivity_send != "") data.productivity = Double.Parse(productivity_send);
        //            if (Ask_leave_send != "") data.Ask_leave = Double.Parse(Ask_leave_send);
        //            if (Overtime_hours_send != "") data.Overtime_hours = Double.Parse(Overtime_hours_send);
        //            if (Start_period_send != "") data.Start_period = Start_period_send;
        //            if (End_period_send != "") data.End_period = End_period_send;
        //            if (effectiveness_H != "") data.effectiveness_H = Double.Parse(effectiveness_H);
        //            if (Vision_send != "") data.vision = (int.Parse(Vision_send))+1;
        //            if(createDate_send != "")data.createDate= Convert.ToDateTime(createDate_send);

        //        ////資料表加入data
        //        db.ProductionDailyReport.Add(data);
        //        ////修改儲存，若沒有這個可能無法如期更改資料表內容
        //        db.SaveChanges();
        //        }
        //    //data.CreateDate = Convert.ToDateTime(time_data);
        //    //data.Vision = Vision_math;

        //    public List<sp_AutoGetERPPartPrice_Result> GetPrice(string Year_Month_Date)
        //    {
        //        List<sp_AutoGetERPPartPrice_Result> List = new List<sp_AutoGetERPPartPrice_Result>();
        //        SyncGTEntities db = new SyncGTEntities();
        //        List = db.sp_AutoGetERPPartPrice(Year_Month_Date).Where(x => x.part != "").ToList();
        //        return List;
        //    }


    }
}