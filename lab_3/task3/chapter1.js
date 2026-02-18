<!DOCTYPE html>
<html>
<body>
    <script>
    function pow(x,n){
      let result=1;
      for(let i=0;i<n;i++) {
          result*=x;
      }
      return result;
   }

    let x=prompt("x?" , " "), n=prompt("n?",'') //сан береміз
    if (n<=0)
{
        alert(` ${n} дәрежесі қате, 0ден үлкен сан енгізіңіз`);
}
    else
{
         alert(pow(x,n))
}
    </script>
</body>
</html>
