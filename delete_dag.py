import sys
from airflow.hooks.postgres_hook import PostgresHook

hook=PostgresHook( postgres_conn_id= "postgres_default")

def confirm_dag_deletion():
    dagidstodelete= input("please input dagid(s) (in case of multiple dags use comma as seperator) to delete: ").split(',')
    confirm = input("[c]Confirm delete or [e]exit: ")
    if confirm != 'c' and confirm != 'e':
        print("\n Invalid Option. Please Enter a Valid Option.")
        return confirm_dag_deletion()
    if confirm == 'e':
        return
    deleteDag(dagidstodelete)
    confirm = input("[c]Continue to delete other dags or [e/anykey]exit: ")
    if confirm == 'c':
        return confirm_dag_deletion()
    return

def deleteDag(dagidstodelete):
    for dagidtodelete in dagidstodelete:
        dagidtodelete = dagidtodelete.strip()
        for t in ["xcom", "task_instance", "sla_miss", "log", "job", "dag_run", "dag" ]:
            sql="delete from {} where dag_id='{}'".format(t, dagidtodelete)
            hook.run(sql, True)

confirm_dag_deletion()