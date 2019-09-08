
class PersonS {
  val id:String = "1234" //val 修饰的属性，系统会自动生成get方法。
  var name:String = "" // var 修饰的属性，系统会自动生成geter & setter方法。

  //private var 修饰的属性，系统会自动生成private修饰的get和set方法。
  private var gender:Int = 0

  //private[this] 修饰的属性，系统不会生成get & set方法。
  //只有当前对象才可以访问该属性。
  private[this] var age:Int = 0

//  def compare(obj:PersonS):Int = {
//    this.age - obj.age
//  }
}

object test{
  def main(args: Array[String]):Unit = {
    var per:PersonS = new PersonS()
    println(per.id)
    per.name_= ("zhangsan")
    println(per.name)
//    println("age:" + per.age)
  }
}
