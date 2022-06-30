function validarRegistro()
{
   var rut = document.formulario.txt_rut.value
   var nombre = document.formulario.txt_nombre.value
   var appaterno = document.formulario.txt_appaterno.value
   var apmaterno = document.formulario.txt_apmaterno.value

   // Validación del Rut
   if (rut.length < 9 || rut.length > 10)
   {
        alert("RUT debe tener entre 9 y 10 caracteres")
        document.formulario.txt_rut.focus()
        return false;
   }

   var Fn = {
    validaRut : function (rutCompleto) {
      rutCompleto = rutCompleto.replace("‐","-");
      if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test( rutCompleto ))
        return false;
      var tmp   = rutCompleto.split('-');
      var digv  = tmp[1]; 
      var rut   = tmp[0];
      if ( digv == 'K' ) digv = 'k' ;
      
      return (Fn.dv(rut) == digv );
    },
    dv : function(T){
      var M=0,S=1;
      for(;T;T=Math.floor(T/10))
        S=(S+T%10*(9-M++%6))%11;
      return S?S-1:'k';
    }
    }

    if (Fn.validaRut( $("#txt_rut").val() )){
        
    } else {
        alert("Formato del Rut incorrecto")
        document.formulario.txt_rut.focus()
        return false;
    }
   
   // Atributos con menos de tres caracteres
   if (nombre.length<3)
   {
       alert("Nombre debe tener al menos 3 caracteres")
       document.formulario.txt_nombre.focus();
       return false;
   }
   if (appaterno.length<3)
   {
       alert("Apellido debe tener al menos 3 caracteres")
       document.formulario.txt_apellido.focus();
       return false;
   }
   if (apmaterno.length<3)
   {
       alert("Comentario debe tener al menos 3 caracteres")
       document.formulario.txa_comentarios.focus()
       return false;
   }

}