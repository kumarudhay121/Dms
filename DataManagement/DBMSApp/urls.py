from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
                     path("AdminLogin.html", views.AdminLogin, name="AdminLogin"),
		     path("AdminLoginAction", views.AdminLoginAction, name="AdminLoginAction"),
		     path("EmployeeManage", views.EmployeeManage, name="EmployeeManage"),
		     path("PatientManage", views.PatientManage, name="PatientManage"),
		     path("Reporting", views.Reporting, name="Reporting"),
		     path("Back", views.Back, name="Back"),
		     path("AddMedicalFacility.html", views.AddMedicalFacility, name="AddMedicalFacility"),
		     path("AddMedicalFacilityAction", views.AddMedicalFacilityAction, name="AddMedicalFacilityAction"),
		     path("AddEmployees.html", views.AddEmployees, name="AddEmployees"),
		     path("AddEmployeesAction", views.AddEmployeesAction, name="AddEmployeesAction"),
		     path("AddInsurance.html", views.AddInsurance, name="AddInsurance"),
		     path("AddInsuranceAction", views.AddInsuranceAction, name="AddInsuranceAction"),
		     path("ViewEmployeeManage", views.ViewEmployeeManage, name="ViewEmployeeManage"),
		     path("ViewMedicalFacility", views.ViewMedicalFacility, name="ViewMedicalFacility"),
		     path("ViewEmployees", views.ViewEmployees, name="ViewEmployees"),
		     path("ViewInsurance", views.ViewInsurance, name="ViewInsurance"),
		     path("PatientManage", views.PatientManage, name="PatientManage"),
		     path("CreatePatient.html", views.CreatePatient, name="CreatePatient"),
		     path("CreatePatientAction", views.CreatePatientAction, name="CreatePatientAction"),
		     path("Appointment.html", views.Appointment, name="Appointment"),
		     path("AppointmentAction", views.AppointmentAction, name="AppointmentAction"),
		     path("UpdatePayment.html", views.UpdatePayment, name="UpdatePayment"),
		     path("UpdatePaymentAction", views.UpdatePaymentAction, name="UpdatePaymentAction"),
		     path("Reporting", views.Reporting, name="Reporting"),
		     path("DayWiseRevenue", views.DayWiseRevenue, name="DayWiseRevenue"),
		     path("DateWiseRevenue", views.DateWiseRevenue, name="DateWiseRevenue"),
		     path("InsuranceRevenue", views.InsuranceRevenue, name="InsuranceRevenue"),
		     path("InsuranceInvoice", views.InsuranceInvoice, name="InsuranceInvoice"),
		     path("DayWiseRevenueAction", views.DayWiseRevenueAction, name="DayWiseRevenueAction"),
		     path("DateWiseRevenueAction", views.DateWiseRevenueAction, name="DateWiseRevenueAction"),
		     path("InsuranceRevenueAction", views.InsuranceRevenueAction, name="InsuranceRevenueAction"),
]