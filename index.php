<?php 
$url = "https://discordapp.com/api/v6/invite/".$_GET["invite"]."?with_counts=true";
$options = array(
'ssl'=>array(
'verify_peer'=>false,
'verify_peer_name'=>false,
)
);
$json = file_get_contents($url,false, stream_context_create($options));
$jsond = json_decode($json,true);
$based64=file_get_contents("https://cdn.discordapp.com/icons/".$jsond['guild']["id"]."/".$jsond['guild']["icon"].".png",false, stream_context_create($options));
$based6=base64_encode($based64);
header('Content-Type: image/svg+xml');
?>

<svg fill="none"  viewBox="0 0 500 110" width="500" height="110" xmlns="http://www.w3.org/2000/svg">
<foreignObject width="100%" height="100%">
<div xmlns="http://www.w3.org/1999/xhtml">
<style>

@font-face{
font-family:Whitney;
font-weight:300;
src:url(https://discordapp.com/assets/6c6374bad0b0b6d204d8d6dc4a18d820.woff) format("woff")
}
@font-face{
font-family:Whitney;
font-weight:400;
src:url(https://discordapp.com/assets/e8acd7d9bf6207f99350ca9f9e23b168.woff) format("woff")
}
@font-face{
font-family:Whitney;
font-weight:500;
src:url(https://discordapp.com/assets/3bdef1251a424500c1b3a78dea9b7e57.woff) format("woff")
}
@font-face{
font-family:Whitney;
font-weight:600;
src:url(https://discordapp.com/assets/be0060dafb7a0e31d2a1ca17c0708636.woff) format("woff")
}
@font-face{
font-family:Whitney;
font-weight:700;
src:url(https://discordapp.com/assets/8e12fb4f14d9c4592eb8ec9f22337b04.woff) format("woff")
}
*{
padding:0;
margin:0;
font:normal normal 600 normal 12px/16px Whitney,"Helvetica Neue",Helvetica,Arial,sans-serif;
outline:0;
text-overflow:ellipsis;
}
@keyframes gradientBackground {
0% {
background-position: 0% 50%;
}
50% {
background-position: 100% 50%;
}
100% {
background-position: 0% 50%;
}
}

.container {

margin: 0;
width: calc(100% - 28px);
height: 80px;
background:#37393e;
padding:10px;
border-radius: 10px;
color: white;
margin-top:5px;
position:relative;
margin-left:4px;
}
.container:before{
content:'';
background: linear-gradient(to right, #6666ff, #0099ff , #00ff00, #ff3399, #6666ff);
height:104px;
width:calc(100% + 5px);
position:absolute;
top:-2px;
left:-2px;
z-index:-1;
border-radius:10px;
animation: rainbow_animation 6s ease-in-out infinite;
background-size: 400% 100%;
}
@keyframes rainbow_animation {
0%,100% {
background-position: 0 0;
}
50% {
background-position: 100% 0;
}
}
h4{
color:#ccc;
}
.imh{
height:50px;
width:50px;
border-radius:15px;
}
.h{
display:flex;
}
.i{
line-height:25px;
font-size:20px;
margin-top:5px;
margin-left:18px;
}
.i span{
display:flex ;
font-size:14px;
color:#72767d;
align-items:center;
justify-content:center;
}
.o,.m{
height:10px;
width:10px;
margin-right:5px;
margin-left:10px;
background:#43b581;
display:block;
border-radius:50%;
}
.m{
margin-left:0;
background:#747f8d;
}
button{
margin-left:20%;
height:40px;
width:80px;
background-color:#3ca374;
border:0;
border-radius:5px;
color:#fff;
}
</style>
<div class="container">
<h4>YOU'VE BEEN INVITED BY <?php echo $jsond['inviter']["username"]?> , TO JOIN A SERVER </h4>
<br/>
<div class="h" ><img class="imh"  src="data:image/png;base64,<?php echo $based6;?>" height="100" width="100"   /><div class="i" > <?php echo $jsond['guild']['name']?><br/><span ><i class="m" ></i><?php echo $jsond['approximate_member_count']?> members <i class="o" ></i><?php echo $jsond['approximate_presence_count']?> Online</span></div><button>Join </button></div>
</div>
</div>
</foreignObject>
</svg>
