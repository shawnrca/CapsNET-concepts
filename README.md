<p><strong>CapsNet</strong></p>
<p>This an implementation of CapsNet for mnist based on the <a href="https://arxiv.org/abs/1710.09829"><strong>Dynamic Routing Between Capsules</strong></a> paper by Sara Sabour, Nicholas Frosst, and Geoffrey E. Hinton.&nbsp; I used tensorflow and mnist data downloaded from <a href="http://yann.lecun.com/exdb/mnist/">Yann LeCun website</a>.</p>
<p>The code is developed Jupyter notebook. I added naive unit tests to make sure the output of each layer is according to specs.&nbsp; I tried to use same name convention for most cases for clarity.</p>
<p>The following is the main architecture of CapsNet.<img src="https://github.com/shawnrca/CapsNET-concepts/blob/master/pics/1.png" alt="" /></p>
<p><img src="https://github.com/shawnrca/CapsNET-concepts/blob/master/pics/1.png" alt="1" /></p>
<p><strong>Convolution layer</strong></p>
<p>&nbsp;It consists of a convolution layer with 256 filters all with 9x9 kernels with stride of 1 with ReLU activation. This results in output 20x20x256.</p>
<p>&nbsp;</p>
<p><strong>Primary capsule layer</strong></p>
<p>It consists of 32 6x6x8 capsules that translates to 32 convolution layers each have 8 filters and 9x9 kernels, stride of 2 and linear activation. The output (<strong>u</strong>) is 32x6x6x8 and is reshaped to 1152x8.&nbsp; 1152 is total capsules outputs.&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><strong>Transformation<br /> <br /> </strong></p>
<p>The output of the primary capsule layer is multiplied by Weight matrix to create <strong>u_hat.&nbsp; </strong>Considering the DigitCaps layer has 10-16D vectors the u_hat will have the shape of 1152x10x16.</p>
<p><strong>&nbsp;</strong></p>
<p><strong>Routing</strong></p>
<p><strong>&nbsp;</strong></p>
<p>At this stage, the logits (<strong>bij</strong>) will be learned through routing algorithms.&nbsp; Logits will be translated to coupling coefficients (<strong>cij</strong>) using softmax function (calculated over DigitCaps). This defines the parent (Digit Caps 1 to 10) that is chosen by each capsule output. So the output is called (<strong>s</strong>). (s) then goes through squash function to create (<strong>v</strong>) with unit norm. &nbsp;Routing algorithm should be executed for each sample in the batch, so I used <strong>tf.while_loop.</strong></p>
<p>&nbsp;</p>
<p>Number of iteration is set to two.&nbsp; The following shows routing algorithm which executed consecutively for every sample in the batch.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><strong>Fully connected (decoder) layer</strong></p>
<p><strong>&nbsp;</strong></p>
<p>This layer reconstructs the input from the DigiCaps layer outputs.&nbsp; This forces the 16D vectors in DigitCaps layer represent the actual digits.&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><strong>&nbsp;</strong></p>
<p><strong>&nbsp;</strong></p>
<p><strong>&nbsp;</strong></p>
<p><strong>&nbsp;</strong></p>
<p><strong>&nbsp;</strong></p>
<p><strong>&nbsp;</strong></p>
<p><strong>&nbsp;</strong></p>
<p><strong>&nbsp;</strong></p>
<p><strong>&nbsp;</strong></p>
<p><strong>Loss</strong></p>
<p>&nbsp;</p>
<p>Loss is combination of margin loss present, margin loss non-present and reconstruction loss with different scalers.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><strong>Optimization</strong></p>
<p>&nbsp;</p>
<p>Adam optimizer is used with default parameters.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><strong>Training</strong></p>
<p>&nbsp;</p>
<p>Training the model with batch size 100 and 5 epochs gave me 0.98% accuracy on test data.&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><strong>Interesting characteristics of coupling coefficients</strong></p>
<p>&nbsp;</p>
<p>After training, I build a graph to visualize how coupling coefficients (<strong>cij</strong>) choose their parent capsules in DigiCaps layer.&nbsp; I used the values for coupling coefficient vectors to visualize the relationship between primary capsules and DigiCaps on a graph. As we can see, primary capsules from different layers are gathered around the DigiCaps.&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
