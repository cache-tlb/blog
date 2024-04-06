---
title: "First_post"
date: 2021-05-06T13:00:39+08:00
categories: ["测试类型"]
showToc: false
toc:
  enable: false
tikz: true
draft: true
---

这是第一个帖子^_^。

- item
- item2
- item3
  - item3/child1
  - item3/child2

{{< rawhtml >}}
  <p class="speshal-fancy-custom">
    This is <strong>raw HTML</strong>, inside Markdown.
  </p>
{{< /rawhtml >}}

测试公式：

$$ \pi = 1 - \dfrac{1}{3} + \dfrac{1}{5} - \dfrac{1}{7} + \cdots $$


{{< tikz >}}  
  \begin{tikzpicture}[cap=round,scale=3.5]
  \definecolor{qqwuqq}{rgb}{0,0.39215686274509803,0}
  \definecolor{ududff}{rgb}{0.30196078431372547,0.30196078431372547,1}
  \definecolor{uuuuuu}{rgb}{0.26666666666666666,0.26666666666666666,0.26666666666666666}  
  \def\a{0}
  \def\b{1}
  \def\c{1.5}
  \def\d{1.875}
  \def\e{2.1875}
  \def\f{2.4609375}
  \def\ab{0.5}
  \def\bc{1.25}
  \def\cd{1.6875}
  \def\de{2.03125}
  \clip(-0.5,-0.15) rectangle (2.8,2.8);
  \def\mylist{0/0,1/1,1.5/{3/2},1.875/{15/8},2.1875/{35/16},2.4609375/{$ \cdots $}}
  \foreach \xx/\label in \mylist{
    \draw [line width=0.5pt,dashed] (0,\xx) -- (10,\xx);
    \draw [line width=0.5pt,dashed] (\xx,0) -- (\xx,10);
    \draw (\xx,-0.03) node[anchor=north] {\label};
    \draw (-0.03,\xx) node[anchor=east] {\label};
  }
  \draw [line width=1pt] (\a,\a) -- (\a,\e) -- (\b,\e) -- (\b,\d) -- (\c,\d) -- (\c,\c) -- (\d,\c) -- (\d,\b) -- (\e,\b) -- (\e,\a) -- (\a,\a) ;
  \draw (\ab,\ab) node {$R_{0,0}$};
  \draw (\ab,\bc) node {$R_{0,1}$};
  \draw (\ab,\cd) node {$R_{0,2}$};
  \draw (\ab,\de) node {$R_{0,3}$};
  \draw (\bc,\ab) node {$R_{1,0}$};
  \draw (\bc,\bc) node {$R_{1,1}$};
  \draw (\bc,\cd) node {$R_{1,2}$};
  \draw (\cd,\ab) node {$R_{2,0}$};
  \draw (\cd,\bc) node {$R_{2,1}$};
  \draw (\de,\ab) node {$R_{3,0}$};
  \def\xx{2.4457}
  \def\yy{2.0252}
  \draw[dashed,red,line width=1pt] (\xx,0) arc [start angle=0, end angle=90, radius=\xx];
  \draw[dashed,green,line width=1pt] (\yy,0) arc [start angle=0, end angle=90, radius=\yy];
  \end{tikzpicture}
  
{{< /tikz >}}


测试 iframe:

<iframe id="viewer" name="viewer" allow="fullscreen; xr-spatial-tracking;" src="https://threejs.org//examples/webgl_animation_keyframes.html" style="width:100%; height:100%"></iframe>


测试 iframe & tikz:

<pre>

<input type="button" onclick="var iFrame = document.getElementById( 'iFrame1' );resizeIFrameToFitContent( iFrame );"> </input>

<iframe id='iFrame1' src="test.html" scrolling="no" type="text/html" onload="var iFrame = document.getElementById( 'iFrame1' );resizeIFrameToFitContent( iFrame );console.log('done');">
</iframe>

<script type="application/javascript">

function resizeIFrameToFitContent( iFrame ) {

    iFrame.width  = iFrame.contentWindow.document.body.scrollWidth;
    iFrame.height = iFrame.contentWindow.document.body.scrollHeight;
}

/*window.addEventListener('DOMContentLoaded', function(e) {

    var iFrame = document.getElementById( 'iFrame1' );
    resizeIFrameToFitContent( iFrame );
} );*/
var observer = new MutationObserver(function(mutations) {
    mutations.forEach(function(mutationRecord) {
        // resizeIFrameToFitContent(mutationRecord.target);
        console.log(mutationRecord.target);
    });    
});

var target = document.getElementById('iFrame1');
observer.observe(target, { subtree: true, childList: true });

</script>

</pre>

LOL

测试 three js
<pre>
<canvas>

</canvas>
</pre>