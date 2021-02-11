class student
{
int sid;
String sname;
int smarks;
}
class Students1
{
public static void main(String a[])
{
student s1=new student();
student s2=new student();
s1.sid=34;
s1.sname="SUSMITHA";
s1.smarks=98;
s2.sid=48;
s2.sname="NAVYA";
s2.smarks=95;
System.out.println(s1.sid);
System.out.println(s1.sname);
System.out.println(s1.smarks);
System.out.println(s2.sid);
System.out.println(s2.sname);
System.out.println(s2.smarks);
}
}