<html>

<head>
<meta http-equiv=Content-Type content="text/html; charset=windows-1252">
<meta name=Generator content="Microsoft Word 15 (filtered)">
<style>
<!--
 /* Font Definitions */
 @font-face
	{font-family:"Cambria Math";
	panose-1:2 4 5 3 5 4 6 3 2 4;}
 /* Style Definitions */
 p.MsoNormal, li.MsoNormal, div.MsoNormal
	{margin:0in;
	margin-bottom:.0001pt;
	line-height:115%;
	font-size:10.0pt;
	font-family:"Arial",sans-serif;
	color:black;}
h1
	{margin-top:20.0pt;
	margin-right:0in;
	margin-bottom:6.0pt;
	margin-left:0in;
	line-height:115%;
	page-break-after:avoid;
	font-size:20.0pt;
	font-family:"Arial",sans-serif;
	color:black;
	font-weight:normal;}
h2
	{margin-top:.25in;
	margin-right:0in;
	margin-bottom:6.0pt;
	margin-left:0in;
	line-height:115%;
	page-break-after:avoid;
	font-size:16.0pt;
	font-family:"Arial",sans-serif;
	color:black;
	font-weight:normal;}
h3
	{margin-top:16.0pt;
	margin-right:0in;
	margin-bottom:4.0pt;
	margin-left:0in;
	line-height:115%;
	page-break-after:avoid;
	font-size:14.0pt;
	font-family:"Arial",sans-serif;
	color:#434343;
	font-weight:normal;}
h4
	{margin-top:14.0pt;
	margin-right:0in;
	margin-bottom:4.0pt;
	margin-left:0in;
	line-height:115%;
	page-break-after:avoid;
	font-size:12.0pt;
	font-family:"Arial",sans-serif;
	color:#666666;
	font-weight:normal;}
h5
	{margin-top:12.0pt;
	margin-right:0in;
	margin-bottom:4.0pt;
	margin-left:0in;
	line-height:115%;
	page-break-after:avoid;
	font-size:11.0pt;
	font-family:"Arial",sans-serif;
	color:#666666;
	font-weight:normal;}
h6
	{margin-top:12.0pt;
	margin-right:0in;
	margin-bottom:4.0pt;
	margin-left:0in;
	line-height:115%;
	page-break-after:avoid;
	font-size:11.0pt;
	font-family:"Arial",sans-serif;
	color:#666666;
	font-weight:normal;
	font-style:italic;}
p.MsoTitle, li.MsoTitle, div.MsoTitle
	{margin-top:0in;
	margin-right:0in;
	margin-bottom:3.0pt;
	margin-left:0in;
	line-height:115%;
	page-break-after:avoid;
	font-size:26.0pt;
	font-family:"Arial",sans-serif;
	color:black;}
p.MsoSubtitle, li.MsoSubtitle, div.MsoSubtitle
	{margin-top:0in;
	margin-right:0in;
	margin-bottom:16.0pt;
	margin-left:0in;
	line-height:115%;
	page-break-after:avoid;
	font-size:15.0pt;
	font-family:"Arial",sans-serif;
	color:#666666;}
.MsoChpDefault
	{font-size:10.0pt;
	font-family:"Arial",sans-serif;
	color:black;}
.MsoPapDefault
	{line-height:115%;}
@page WordSection1
	{size:8.5in 11.0in;
	margin:1.0in 1.0in 1.0in 1.0in;}
div.WordSection1
	{page:WordSection1;}
-->
</style>

</head>

<body lang=EN-US>

<div class=WordSection1>

<p class=MsoNormal><b><span lang=EN style='font-size:30.0pt;line-height:115%'>CapsNet</span></b></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>This an implementation of CapsNet for mnist
based on the <a href="https://arxiv.org/abs/1710.09829"><b><span
style='color:#1155CC'>Dynamic Routing Between Capsules</span></b></a> paper by
Sara Sabour, Nicholas Frosst, and Geoffrey E. Hinton.  I used tensorflow and
mnist data downloaded from <a href="http://yann.lecun.com/exdb/mnist/"><span
style='color:#1155CC'>Yann LeCun website</span></a>.</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>The code is developed Jupyter notebook. I
added naive unit tests to make sure the output of each layer is according to
specs.  I tried to use same name convention for most cases for clarity.</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>The following is the main architecture of
CapsNet. </span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><img border=0 width=624 height=168 id=image11.png
src="article%20on%20capsnet_files/image001.png"></p>

<p class=MsoNormal><b><span lang=EN>Convolution layer</span></b><span lang=EN> </span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>It consists of a convolution layer with 256
filters all with 9x9 kernels with stride of 1 with ReLU activation. This
results in output 20x20x256.</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><img border=0 width=623 height=160 id=image5.png
src="article%20on%20capsnet_files/image002.png"></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>Primary capsule layer</span></b></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>It consists of 32 6x6x8 capsules that
translates to 32 convolution layers each have 8 filters and 9x9 kernels, stride
of 2 and linear activation. The output (<b>u</b>) is 32x6x6x8 and is reshaped
to 1152x8.  1152 is total capsules outputs.  </span></p>

<p class=MsoNormal><span lang=EN> </span></p>

<p class=MsoNormal><img border=0 width=624 height=150 id=image6.png
src="article%20on%20capsnet_files/image003.png"><span lang=EN><a
href="https://arxiv.org/find/cs/1/au:+Hinton_G/0/1/0/all/0/1"></a></span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><b><span lang=EN>Transformation<br>
<br>
</span></b></p>

<p class=MsoNormal><span lang=EN>The output of the primary capsule layer is
multiplied by Weight matrix to create <b>u_hat.  </b>Considering the DigitCaps
layer has 10-16D vectors the u_hat will have the shape of 1152x10x16.</span></p>

<p class=MsoNormal><span style='font-size:48.0pt;line-height:115%'><img
border=0 width=624 height=190 id=image2.png
src="article%20on%20capsnet_files/image004.png"></span></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>Routing</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><span lang=EN>At this stage, the logits (<b>bij</b>) will be
learned through routing algorithms.  Logits will be translated to coupling coefficients
(<b>cij</b>) using softmax function (calculated over DigitCaps). This defines
the parent (Digit Caps 1 to 10) that is chosen by each capsule output. So the
output is called (<b>s</b>). (s) then goes through squash function to create (<b>v</b>)
with unit norm.  Routing algorithm should be executed for each sample in the
batch, so I used <b>tf.while_loop.</b></span></p>

<p class=MsoNormal><span lang=EN> </span><img border=0 width=592 height=155
id=image10.png src="article%20on%20capsnet_files/image005.png"></p>

<p class=MsoNormal><span lang=EN>Number of iteration is set to two.  The
following shows routing algorithm which executed consecutively for every sample
in the batch.</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><img border=0 width=625 height=222 id=image12.png
src="article%20on%20capsnet_files/image006.png"> </p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><b><span lang=EN>Fully connected (decoder) layer</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><span lang=EN>This layer reconstructs the input from the
DigiCaps layer outputs.  This forces the 16D vectors in DigitCaps layer
represent the actual digits.  </span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><img border=0 width=623 height=300 id="Picture 7"
src="article%20on%20capsnet_files/image007.jpg"></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>&nbsp;</span></b></p>

<p class=MsoNormal><b><span lang=EN>Loss</span></b></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>Loss is combination of margin loss present,
margin loss non-present and reconstruction loss with different scalers.</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><img border=0 width=624 height=294 id="Picture 8"
src="article%20on%20capsnet_files/image008.jpg"></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><b><span lang=EN>Optimization</span></b></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>Adam optimizer is used with default
parameters. </span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><img border=0 width=364 height=63 id="Picture 9"
src="article%20on%20capsnet_files/image009.jpg"></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><b><span lang=EN>Training</span></b></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>Training the model with batch size 100 and 5
epochs gave me 0.98% accuracy on test data.  </span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><b><span lang=EN>Interesting characteristics of coupling
coefficients</span></b></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>After training, I build a graph to visualize
how coupling coefficients (<b>cij</b>) choose their parent capsules in DigiCaps
layer.  I used the values for coupling coefficient vectors to visualize the
relationship between primary capsules and DigiCaps on a graph. As we can see,
primary capsules from different layers are gathered around the DigiCaps.  </span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><img border=0 width=558 height=502 id="Picture 10"
src="article%20on%20capsnet_files/image010.jpg"></p>

<p class=MsoNormal><span lang=EN>&nbsp;</span></p>

<p class=MsoNormal><span lang=EN style='font-size:48.0pt;line-height:115%'>&nbsp;</span></p>

</div>

</body>

</html>
