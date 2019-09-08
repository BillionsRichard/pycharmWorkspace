class AccountInfo {
  var id = AccountInfo.newUniqueNumber
}

//类的伴生对象。伴生对象和类可以互相访问彼此的私有属性或方法。
object AccountInfo{
  private var lastNumber = 0
  private def newUniqueNumber:Int = {
    lastNumber += 1
    lastNumber
  }
}

//object companionTest{
//  def main(args: Array[String]): Unit = {
//    var obj:AccountInfo = new AccountInfo()
//    println(obj.id)
//
//  }
//}

//应用程序对象
object companionTest extends App{
  var obj:AccountInfo = new AccountInfo()
      println(obj.id)
}