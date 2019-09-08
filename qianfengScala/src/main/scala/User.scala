class User(var name:String, val password:String) {

}

object User{
  def apply(name:String, password:String) = new User(name, password)

}

object userTest{
  def main(args: Array[String]): Unit = {
//    val obj = new User("zhangsam", "123")
    val obj = User("zhangsam", "123")
    println("result: " + obj.isInstanceOf[User])
  }
}
