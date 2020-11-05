  <div id="jigsaw-shortcut-lists">



</div>

<h1 class="gap">0x00. AirBnB clone - The console</h1>


<div id="project_id" style="display: none" data-project-id="263"></div>

<p class="sm-gap">
  <small>
    <i class="fa fa-folder-open"></i>
    Foundations - Higher-level programming ― AirBnB clone
  </small>
</p>

  <p>
    <em>
      <small>
        <i class="fa fa-user"></i> by Guillaume, CTO at Holberton School
      </small>
    </em>
  </p>

<div class="gap formatted-content">
    <p style="margin-bottom: 0"><em>For this project, students are expected to look at these concepts:</em></p>
    <ul style="margin-top: 5px">
        <li>
        <em><a href="/concepts/66">Python packages</a></em>
        </li>
        <li>
        <em><a href="/concepts/74">AirBnB clone</a></em>
        </li>
    </ul>
</div>

  <article id="description" class="gap formatted-content">
    <p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201105%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201105T003823Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7dfc048104d2fec284080b56109d9013c767c000f6af8dafe1fcd43cba036c67" alt="" style="" /></p>

<h2>Background Context</h2>

<h3>Welcome to the AirBnB clone project! (The Holberton B&amp;B)</h3>

<p>Before starting, please read the <strong>AirBnB</strong> concept page.</p>

<p><br/></p>

<a href="https://www.youtube.com/embed/E12Xc3H2xqo" title="HBNB project overview" target="_blank">HBNB project overview</a>

<p><br/></p>

<h4>First step: Write a command interpreter to manage your AirBnB objects.</h4>

<p>This is the first step towards building your first full web application: the <strong>AirBnB clone</strong>.
This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration&hellip; </p>

<p>Each task is linked and will help you to:</p>

<ul>
<li>put in place a parent class (called <code>BaseModel</code>) to take care of the initialization, serialization and deserialization of your future instances</li>
<li>create a simple flow of serialization/deserialization: Instance &lt;-&gt; Dictionary &lt;-&gt; JSON string &lt;-&gt; file</li>
<li>create all classes used for AirBnB (<code>User</code>, <code>State</code>, <code>City</code>, <code>Place</code>&hellip;) that inherit from <code>BaseModel</code></li>
<li>create the first abstracted storage engine of the project: File storage. </li>
<li>create all unittests to validate all our classes and storage engine</li>
</ul>

<h3>What&rsquo;s a command interpreter?</h3>

<p>Do you remember the Shell? It&rsquo;s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:</p>

<ul>
<li>Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc&hellip;</li>
<li>Do operations on objects (count, compute stats, etc&hellip;)</li>
<li>Update attributes of an object</li>
<li>Destroy an object</li>
</ul>

<h2>Resources</h2>

<p><strong>Read or watch</strong>:</p>

<ul>
<li><a href="/rltoken/Fx9HXIjmGzbmET4ylYg2Rw" title="cmd module" target="_blank">cmd module</a> </li>
<li><strong>packages</strong> concept page</li>
<li><a href="/rltoken/eaQ6aELbdqb0WmPddhD00g" title="uuid module" target="_blank">uuid module</a> </li>
<li><a href="/rltoken/_ySDcgtfrwLkTyQzYHTH0Q" title="datetime" target="_blank">datetime</a> </li>
<li><a href="/rltoken/QX7d4D__xhOJIGIWZBp39g" title="unittest module" target="_blank">unittest module</a> </li>
<li><a href="/rltoken/jQd3P_uSO0FeU6jlN-z5mg" title="args/kwargs" target="_blank">args/kwargs</a> </li>
<li><a href="/rltoken/WPlydsqB0PG0uVcixemv9A" title="Python test cheatsheet" target="_blank">Python test cheatsheet</a> </li>
</ul>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/MwKclAaCLNksSms8I-LuXw" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>How to create a Python package</li>
<li>How to create a command interpreter in Python using the <code>cmd</code> module</li>
<li>What is Unit testing and how to implement it in a large project</li>
<li>How to serialize and deserialize a Class</li>
<li>How to write and read a JSON file</li>
<li>How to manage <code>datetime</code></li>
<li>What is an <code>UUID</code></li>
<li>What is <code>*args</code> and how to use it</li>
<li>What is <code>**kwargs</code> and how to use it</li>
<li>How to handle named arguments in a function</li>
</ul>


<h2>More Info</h2>

<h3>Execution</h3>

<p>Your shell should work like this in interactive mode:</p>

<pre><code>$ ./console.py
(hbnb) help

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
</code></pre>

<p>But also in non-interactive mode: (like the Shell project in C)</p>

<pre><code>$ echo &quot;help&quot; | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
</code></pre>

<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201105%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201105T003823Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8c8afbfe90be2776fedd8067aaba93d0f346a3ba9e2aa4cd9c2ac9a3433ba583" alt="" style="" /></p>

<p><br /></p>

<a href="https://www.youtube.com/embed/p00ES-5K4C8" title="HBNB - The console" target="_blank">HBNB - The console</a>
