//单例对象
//Java中的工具类，定义工具函数和常量
//单例对象不能带参数.
object Logger {

    def log(msg:String):Unit = {
      println(s"INFO:$msg")
    }
}

class Test{
  def method:Unit = {
    Logger.log("hello")
  }
}

object LoggerTest{
  def main(args: Array[String]): Unit = {
    Logger.log("haha")
    val obj:Test = new Test()
    obj.method
  }
}