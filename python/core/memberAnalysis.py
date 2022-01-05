"""
    Author : Hashani Elion
    Mail : elion.hashani@telecomnancy.eu
    Date : 27/12/2021
"""

# Import neded packages
import sqlite3

jobAbrev={'Agriculteur exploitant' : "agriexp" ,
    "Artisan, Commerçant, Chef d'entreprise" : "artcomchef",
    'Cadre, Profession intellectuelle supérieure' : "cadreprofintsup",
    'Profession intermédiaire' : "profintermed",
    'Employé' : "employe",
    'Ouvrier' : "ouvrier",
    'Retraité' : "retraite",
    'Sans activité professionnelle' : "sansactprof"
    }

jobGrades={"agriexp" : 0
        ,"artcomchef" : 0
        ,"cadreprofintsup" : 0
        ,"profintermed" : 0
        ,"employe" : 0
        ,"ouvrier" : 0
        ,"retraite" : 0
        ,"sansactprof" : 0
        }

jobList=["agriexp"
        ,"artcomchef"
        ,"cadreprofintsup"
        ,"profintermed"
        ,"employe"
        ,"ouvrier"
        ,"retraite"
        ,"sansactprof"]

def rateList(session_id: int)->None:
    requestQuery='''SELECT listId FROM Candidate WHERE id=?;'''
    arg = (session_id, )
                
    db = sqlite3.connect('database.db')
    cursor = db.cursor()

    cursor.execute(requestQuery, arg)
    listId = cursor.fetchall()[0][0]

    totalQuery='''SELECT COUNT(*) FROM Member WHERE listId=?;'''
    totalArg=(listId,)
    cursor.execute(totalQuery,totalArg)  
    totalMembers=cursor.fetchall()[0][0]

    totQuery='''SELECT COUNT(firstName), job FROM Member WHERE listId=? GROUP BY job;'''
    totArg=(listId,)
    cursor.execute(totQuery,totArg)  
    totMembers=cursor.fetchall()

    L=[]
    for k in range(len(totMembers)):
        L.append(jobAbrev[totMembers[k][1]])
        jobGrades[jobAbrev[totMembers[k][1]]]=totMembers[k][0]/totalMembers*100
    
    job0=list(set(jobList)-set(L))
    for i in range(len(job0)):
        jobGrades[job0[i]]=0

    updateQuery='''UPDATE jobMemberGrade SET agriexp=?,artcomchef=?,cadreprofintsup=?,profintermed=?,employe=?,ouvrier=?,retraite=?,sansactprof=? WHERE listId=?'''
    updateArg=(round(jobGrades["agriexp"],2),round(jobGrades["artcomchef"],2),round(jobGrades["cadreprofintsup"],2),round(jobGrades["profintermed"],2),round(jobGrades["employe"],2),round(jobGrades["ouvrier"],2),round(jobGrades["retraite"],2),round(jobGrades["sansactprof"],2),listId)

    cursor.execute(updateQuery,updateArg)

    db.commit()
    cursor.close()
    db.close()

