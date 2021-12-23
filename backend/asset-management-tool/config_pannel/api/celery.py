import os
from celery import Celery
import nepali_datetime
import datetime

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asset_management_system.settings')

app = Celery('config_pannel')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


def add_day_to_date(date, days):
    '''Return new date after adding days to given date'''
    from datetime import datetime,timedelta
    date = date + timedelta(days=days)
    return date
     
@app.task(bind=True)
def income_notify(self):
    '''Notification for income last created'''
    from finance.models import Income
    import time
    from users.models import Users
    from config_pannel.models import NotificationPeriod, NotificationStore
    import humanize
    from asset_management_system.pusher import sendPushNotification
    care_taker = Users.objects.filter(is_care_taker=True)
    for i in care_taker:
        notification_config = NotificationPeriod.objects.filter(water_scheme = i.water_scheme).last()
        if notification_config:
            if notification_config.last_income_push:
                date =notification_config.last_income_push
            else:
                date = notification_config.initial_date
            days =notification_config.income_notification_period
            push_notification_date =add_day_to_date(date, days)

            if push_notification_date <= datetime.date.today():
                last_income = Income.objects.filter(category__water_scheme = i.water_scheme).last()
                title = 'Income'
                title_np = 'आय'
                notf_type = 'cashbook'
                if last_income:
                    dt = datetime.date(last_income.created_at.year,last_income.created_at.month,last_income.created_at.day)
                    message = 'Last income was created at '+ str(dt)#str(humanize.naturalday(last_income.created_at)) + '.'
                    message_np = 'पछिल्लो आय सम्पन्न मिति '+ str(nepali_datetime.date.from_datetime_date(dt))
                else:
                    message = 'You have not added any income record.'
                    message_np = 'तपाईंले पछिल्लो आय थप्नु भएको छैन'
            
                notification_config.last_income_push = push_notification_date
                notification_config.save()
                notf = NotificationStore.objects.create(water_scheme=i.water_scheme,message=message, message_np=message_np,title=title, title_np=title_np, notf_type=notf_type)
                sendPushNotification(notf.id, notf.created_date, title, message, message_np, title_np, i.water_scheme.slug,notf_type)
                time.sleep(2)

@app.task(bind=True)
def expense_notify(self):
    '''Notification for expenditure last created.'''
    from finance.models import Expenditure
    from users.models import Users
    from config_pannel.models import NotificationPeriod, NotificationStore
    from asset_management_system.pusher import sendPushNotification
    import humanize
    import time
    care_taker = Users.objects.filter(is_care_taker=True)
    for i in care_taker:
        notification_config = NotificationPeriod.objects.filter(water_scheme = i.water_scheme).last()
        if notification_config:
            if notification_config.last_expense_push:
                date =notification_config.last_expense_push
            else:
                date = notification_config.initial_date
            days =notification_config.expenditure_notification_period
            push_notification_date =add_day_to_date(date, days)

            if push_notification_date <= datetime.date.today():
                last_expense = Expenditure.objects.filter(category__water_scheme = i.water_scheme).last()
                title = 'Expenditure'
                title_np = 'खर्च'
                notf_type = 'cashbook'
                if last_expense:
                    dt = datetime.date(last_expense.created_at.year,last_expense.created_at.month,last_expense.created_at.day)
                    message = 'Last expenditure was created at '+ str(dt)#str(humanize.naturalday(last_income.created_at)) + '.'
                    message_np = 'पछिल्लो खर्च सम्पन्न मिति '+ str(nepali_datetime.date.from_datetime_date(dt))
                else:
                    message = 'You have not added any expenditure record.'
                    message_np = 'तपाईंले पछिल्लो खर्च थप्नु भएको छैन'

                notification_config.last_expense_push = push_notification_date
                notification_config.save()
                notf = NotificationStore.objects.create(water_scheme=i.water_scheme,message=message, message_np=message_np,title=title, title_np=title_np, notf_type = notf_type)
                sendPushNotification(notf.id, notf.created_date, title, message, message_np, title_np, i.water_scheme.slug,notf_type)
                time.sleep(2)

@app.task(bind=True)
def supply_record_notify(self):
    '''Notification for water supply record last created.'''
    from users.models import Users
    from config_pannel.models import NotificationPeriod, WaterSupplyRecord, NotificationStore
    from asset_management_system.pusher import sendPushNotification
    import humanize
    import time
    care_taker = Users.objects.filter(is_care_taker=True)
    for i in care_taker:
        notification_config = NotificationPeriod.objects.filter(water_scheme = i.water_scheme).last()
        if notification_config:
            if notification_config.last_water_record_push:
                date =notification_config.last_water_record_push
            else:
                date = notification_config.initial_date
            days =notification_config.supply_record_notification_period
            push_notification_date =add_day_to_date(date, days)
            if push_notification_date <= datetime.date.today():
                data = WaterSupplyRecord.objects.filter(water_scheme = i.water_scheme).last()
                title = 'Water supply record'
                title_np = 'पानी आपूर्ति रेकर्ड'
                notf_type = 'service'
                if data:
                    dt = datetime.date(data.created_at.year,data.created_at.month,data.created_at.day)
                    message = 'Last water supply record was created at '+ str(dt)#str(humanize.naturalday(last_income.created_at)) + '.'
                    message_np = 'पछिल्लो पानी आपूर्ति रेकर्ड मा सिर्जना गरिएको  मिति'+ str(nepali_datetime.date.from_datetime_date(dt))
                else:
                    message = 'You have not added any water supply record.'
                    message_np = 'तपाईंले कुनै पनि पानी आपूर्ति रेकर्ड थप्नु भएको छैन'
                notification_config.last_water_record_push = push_notification_date
                notification_config.save()
                notf = NotificationStore.objects.create(water_scheme=i.water_scheme,message=message, message_np=message_np,title=title, title_np=title_np, notf_type=notf_type)
                sendPushNotification(notf.id, notf.created_date, title, message, message_np, title_np, i.water_scheme.slug, notf_type)
                time.sleep(6)

@app.task(bind=True)
def test_result_notify(self):
    '''Notification for water test result last created'''
    from users.models import Users
    from config_pannel.models import NotificationPeriod, WaterTestResults, NotificationStore
    from asset_management_system.pusher import sendPushNotification
    import humanize
    import time

    care_taker = Users.objects.filter(is_care_taker=True)
    for i in care_taker:
        notification_config = NotificationPeriod.objects.filter(water_scheme = i.water_scheme).last()

        if notification_config:
            if notification_config.last_test_result_push:
                date =notification_config.last_test_result_push
            else:
                date = notification_config.initial_date
            days =notification_config.supply_record_notification_period
            push_notification_date =add_day_to_date(date, days)
            if push_notification_date <= datetime.date.today():
                data = WaterTestResults.objects.filter(water_scheme = i.water_scheme).last()
                title = 'Water test result'
                title_np = 'पानी परीक्षण परिणाम'
                notf_type = 'service'
                if data:
                    dt = datetime.date(data.created_at.year,data.created_at.month,data.created_at.day)
                    message = 'Last water supply record was created at '+ str(dt)#str(humanize.naturalday(last_income.created_at)) + '.'
                    message_np = 'पछिल्लो पानी परीक्षण परिणाम सिर्जना गरिएको मिति'+ str(nepali_datetime.date.from_datetime_date(dt))
                else:
                    message = 'You have not added any water supply record.'
                    message_np = 'तपाईंले कुनै पनि पानी परीक्षण परिणाम थप्नु भएको छैन'
                notification_config.last_test_result_push = push_notification_date
                notification_config.save()
                notf = NotificationStore.objects.create(water_scheme=i.water_scheme,message=message, message_np=message_np,title=title, title_np=title_np, notf_type=notf_type)
                sendPushNotification(notf.id, notf.created_date, title, message, message_np, title_np, i.water_scheme.slug, notf_type)
                time.sleep(2)

@app.task(bind=True)
def alert_caretaker_for_maintenance_log_creation(self):
    '''Notification for maintenance log creation.'''
    from users.models import Users
    from maintenance.models import ComponentInfo
    from asset_management_system.pusher import sendPushNotification
    from config_pannel.models import NotificationStore,YearsInterval
    from maintenance.api.utils import add_months

    care_taker = Users.objects.filter(is_care_taker=True)
    for i in care_taker:
        current_year_interval = YearsInterval.objects.get(scheme = i.water_scheme).only('start_date')
        info = ComponentInfo.objects.filter(component__category__water_scheme = i.water_scheme, maintenance_interval__lte = 1, apply_date__lte  = current_year_interval.start_date).values('id','next_action','maintenance_interval','component__name')
        data_list  = []
        for j in info:
            data = {}
            next_action = j.get('next_action')
            maintenance_interval = j.get('maintenance_interval')
            total_logs = int(1/maintenance_interval)
            next_action_month_interval = int(12/total_logs)
            data['next_action'] = str(next_action)
            data['component__name']=j.get('component__name')
            data_list.append(data)
            if total_logs >=1:
                for logs in range(total_logs):
                    data = {}
                    data['next_action'] = str(add_months(next_action,next_action_month_interval))
                    data['component__name']=j.get('component__name')
                    data_list.append(data)
       
        diff = get_factors_of(current_year_interval.year_num)
        component2 = ComponentInfo.objects.filter(component__category__water_scheme = i.water_scheme, maintenance_interval__gt = 1,maintenance_interval__in =diff, apply_date__lte  = current_year_interval.start_date,).values('id','next_action','maintenance_interval','component__name')
        if component2:
            for comp2 in component2:
                data = {}
                next_action = comp2.get('next_action').replace(year=current_year_interval.year)
                data['next_action'] = str(next_action)
                data['component__name']=comp2.get('component__name')
                data_list.append(data)
        
        for data in data_list:
            tod = data.get('next_action')
            d = datetime.timedelta(days = 5)
            a = tod - d
            b= tod + d
            tod_dt = datetime.date(tod.created_at.year,tod.created_at.month,tod.created_at.day)
            tod_np=str(nepali_datetime.date.from_datetime_date(tod_dt))
            
            title = 'Next Maintenance'
            title_np = 'अर्को मर्मतसम्भार'
            notf_type = 'maintenance'
            if str(datetime.datetime.now().date()) == str(a):
                message = data.get('component__name') + ' has maintenance on '+ tod
                message_np  =data.get('component__name') + ' मर्मत मिति '+ tod_np
                notf = NotificationStore.objects.create(water_scheme=i.water_scheme,message=message, message_np=message_np,title=title, title_np=title_np,notf_type=notf_type)
            elif str(datetime.datetime.now().date()) == str(data.get('next_action')):
                message = data.get('component__name') + ' has maintenance on '+ tod
                message_np  =data.get('component__name') + ' मर्मत मिति '+ tod_np
                notf = NotificationStore.objects.create(water_scheme=i.water_scheme,message=message, message_np=message_np,title=title, title_np=title_np,notf_type=notf_type)
            elif str(datetime.datetime.now().date()) == str(a):
                message = data.get('component__name') + ' has maintenance on '+ tod
                message_np  =data.get('component__name') + ' मर्मत मिति '+ tod_np
                notf = NotificationStore.objects.create(water_scheme=i.water_scheme,message=message, message_np=message_np,title=title, title_np=title_np,notf_type=notf_type)
        sendPushNotification(notf.id, notf.created_date, title, message, message_np, title_np, i.water_scheme.slug, notf_type)
                    
       
