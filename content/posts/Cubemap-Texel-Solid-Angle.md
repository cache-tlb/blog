---
title: "Cubemap上每像素对应的立体角计算"
date: 2022-05-10T20:02:31+08:00
categories: ["数学"]
---

在处理环境光的重要性采样时, 具体的采样算法依赖于环境光的表达方式, 例如环境光可以用 cubemap, 全景图(panorama image), 或者球谐函数(spherical harmonics)表示. 
对于前两者, 不能简单用像素亮度值作为权重来采样.

以全景图为例, 一般全景图的像素是将 $[0,2\pi]\times[0,\pi]$ 经纬度的参数空间均匀划分, 如此两极附近的像素密度是高于赤道附近的像素密度的, 或者说两极附近每像素对应的立体角小于赤道附近每像素对应的立体角.
考虑极端情况, 整个全景图所有像素值都相等, 若仅考虑像素亮度值, 则每个像素被采样的概率都相等, 这将导致两极附近的样本多于赤道的. 因此需要根据像素的立体角对采样概率进行修正. 就比如以一个分段常量函数为采样的pdf, 每段的区间范围不一样, 不仅要考虑区间的高度, 也要考虑区间的宽度.

对全景图来说, 每像素立体角是容易计算的, 假设像素的覆盖区域是 $[\theta_1, \theta_2]\times[\phi_1,\phi_2]$, 其中 $\theta_1,\theta_2\in [0,2\pi]$, $\phi_1,\phi_2\in [0,\pi]$, $\phi=0$为北极点$(0,0,1)$, $\phi=\pi/2$为赤道, $\phi=\pi$ 为南极点$(0,0,-1)$, 那么该像素对应的立体角为
$$
\Omega = \int_{\phi_1}^{\phi_2}{\int_{\theta_1}^{\theta_2} {\sin\phi}\ \mathrm{d}\theta}\ \mathrm{d}\phi = (\theta_2 - \theta_1)(\cos\phi_1 - \cos\phi_2) .
$$

对于 cubemap 的情况也一样, 虽然 cubemap 上不同像素对的立体角的差异不如全景图那么大, 但也还是有的. 已经有文章分析了思路([链接在此](https://www.rorydriscoll.com/2012/01/15/cubemap-texel-solid-angle/)), 但没有给出积分的推导过程. 本文在此对过程做一些补充.

轴对齐的正方体中心位于原点, 边长为 2, 每个面上有一张正方形的纹理, 像素数为 $N\times N$. 相机位于原点. 考虑位于 $z=-1$ 平面上的正方形, $x,y$的范围都是 $[-1,1]$, 其上每个像素虽然面积一样, 但是所占据的视角大小不同, 例如靠近中心的像素对应的视角大于边缘像素对应的视角范围. 用立体角衡量视角的大小, 将面积元投影到以相机为球心的单位球面上, 投影面积就是立体角的大小.

<div>
<center>
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="450pt" height="300pt" viewBox="50 75 350 275" version="1.1">
<defs>
<g>
<symbol overflow="visible" id="glyph0-0">
<path style="stroke:none;" d=""/>
</symbol>
<symbol overflow="visible" id="glyph0-1">
<path style="stroke:none;" d="M 1.453125 -0.875 C 1.984375 -1.453125 2.265625 -1.703125 2.6875 -2.046875 C 2.6875 -2.140625 3.25 -2.546875 3.609375 -2.90625 C 4.5625 -3.84375 4.828125 -4.421875 4.828125 -4.46875 C 4.828125 -4.5625 4.5625 -4.734375 4.546875 -4.734375 C 4.46875 -4.734375 4.3125 -4.671875 4.265625 -4.578125 C 3.96875 -4.09375 3.890625 -3.984375 3.65625 -3.984375 C 3.40625 -3.984375 3.40625 -4.09375 3.265625 -4.25 C 3.078125 -4.484375 2.78125 -4.734375 2.453125 -4.734375 C 1.703125 -4.734375 1.0625 -3.640625 1.0625 -3.421875 C 1.0625 -3.375 1.28125 -3.15625 1.359375 -3.15625 C 1.453125 -3.15625 1.640625 -3.375 1.671875 -3.421875 C 1.859375 -3.890625 2.265625 -3.734375 2.34375 -3.734375 C 2.546875 -3.734375 2.734375 -3.671875 2.96875 -3.59375 C 3.375 -3.4375 3.484375 -3.4375 3.375 -3.4375 C 3.25 -3.296875 2.40625 -2.578125 2.21875 -2.40625 L 1.328125 -1.578125 C 0.640625 -0.90625 0.25 -0.21875 0.25 -0.15625 C 0.25 -0.046875 0.53125 0.109375 0.546875 0.109375 C 0.625 0.109375 0.765625 0.046875 0.828125 -0.0625 C 1.0625 -0.421875 1.234375 -0.640625 1.5625 -0.640625 C 1.78125 -0.640625 1.75 -0.59375 2 -0.3125 C 2.171875 -0.09375 2.484375 0.109375 2.765625 0.109375 C 3.765625 0.109375 4.5 -1.3125 4.5 -1.578125 C 4.5 -1.640625 4.296875 -1.859375 4.21875 -1.859375 C 4.125 -1.859375 3.921875 -1.625 3.890625 -1.5625 C 3.671875 -0.90625 3.203125 -0.890625 2.875 -0.890625 C 2.6875 -0.890625 2.5 -0.953125 2.296875 -1.015625 C 1.953125 -1.140625 1.796875 -1.1875 1.59375 -1.1875 C 1.578125 -1.1875 1.421875 -1.1875 1.328125 -1.15625 Z M 1.453125 -0.875 "/>
</symbol>
<symbol overflow="visible" id="glyph0-2">
<path style="stroke:none;" d="M 3.5 -3.171875 C 3.5625 -3.421875 3.625 -4.1875 4.3125 -4.1875 C 4.359375 -4.1875 4.46875 -4.234375 4.6875 -4.109375 L 4.8125 -4.390625 C 4.53125 -4.34375 4.15625 -3.921875 4.15625 -3.671875 C 4.15625 -3.515625 4.453125 -3.171875 4.71875 -3.171875 C 4.9375 -3.171875 5.421875 -3.515625 5.421875 -3.90625 C 5.421875 -4.421875 4.671875 -4.734375 4.328125 -4.734375 C 3.75 -4.734375 3.265625 -4.15625 3.296875 -4.203125 C 3.203125 -4.46875 2.5 -4.734375 2.203125 -4.734375 C 1.171875 -4.734375 0.421875 -3.28125 0.421875 -3.03125 C 0.421875 -2.9375 0.703125 -2.765625 0.71875 -2.765625 C 0.796875 -2.765625 1 -2.953125 1.015625 -3.046875 C 1.359375 -4.09375 1.84375 -4.1875 2.1875 -4.1875 C 2.375 -4.1875 2.546875 -4.25 2.546875 -3.671875 C 2.546875 -3.375 2.375 -2.703125 2 -1.3125 C 1.84375 -0.6875 1.671875 -0.4375 1.234375 -0.4375 C 1.171875 -0.4375 1.0625 -0.390625 0.859375 -0.515625 L 0.734375 -0.234375 C 0.984375 -0.296875 1.375 -0.65625 1.375 -0.9375 C 1.375 -1.203125 0.984375 -1.453125 0.84375 -1.453125 C 0.53125 -1.453125 0.109375 -1.03125 0.109375 -0.703125 C 0.109375 -0.25 0.78125 0.109375 1.21875 0.109375 C 1.890625 0.109375 2.359375 -0.640625 2.390625 -0.703125 L 2.09375 -0.8125 C 2.21875 -0.4375 2.75 0.109375 3.34375 0.109375 C 4.375 0.109375 5.109375 -1.328125 5.109375 -1.578125 C 5.109375 -1.6875 4.859375 -1.859375 4.828125 -1.859375 C 4.734375 -1.859375 4.53125 -1.640625 4.515625 -1.578125 C 4.1875 -0.515625 3.6875 -0.4375 3.375 -0.4375 C 2.984375 -0.4375 2.984375 -0.59375 2.984375 -0.921875 C 2.984375 -1.140625 3.046875 -1.359375 3.15625 -1.796875 Z M 3.5 -3.171875 "/>
</symbol>
<symbol overflow="visible" id="glyph0-3">
<path style="stroke:none;" d="M 5.015625 -3.953125 C 5.046875 -4.09375 5.046875 -4.109375 5.046875 -4.1875 C 5.046875 -4.359375 4.75 -4.625 4.59375 -4.625 C 4.5 -4.625 4.203125 -4.515625 4.109375 -4.34375 C 4.046875 -4.203125 3.96875 -3.890625 3.921875 -3.703125 C 3.859375 -3.453125 3.78125 -3.1875 3.734375 -2.90625 L 3.28125 -1.109375 C 3.234375 -0.96875 2.984375 -0.4375 2.328125 -0.4375 C 1.828125 -0.4375 1.890625 -0.703125 1.890625 -1.078125 C 1.890625 -1.53125 2.046875 -2.15625 2.390625 -3.03125 C 2.546875 -3.4375 2.59375 -3.546875 2.59375 -3.75 C 2.59375 -4.203125 2.109375 -4.734375 1.609375 -4.734375 C 0.65625 -4.734375 0.109375 -3.125 0.109375 -3.03125 C 0.109375 -2.9375 0.390625 -2.765625 0.40625 -2.765625 C 0.515625 -2.765625 0.6875 -2.953125 0.734375 -3.109375 C 1 -4.046875 1.234375 -4.1875 1.578125 -4.1875 C 1.65625 -4.1875 1.640625 -4.34375 1.640625 -4.03125 C 1.640625 -3.78125 1.546875 -3.515625 1.46875 -3.328125 C 1.078125 -2.265625 0.890625 -1.703125 0.890625 -1.234375 C 0.890625 -0.34375 1.703125 0.109375 2.296875 0.109375 C 2.6875 0.109375 3.140625 -0.109375 3.421875 -0.390625 L 3.125 -0.5 C 2.984375 0.015625 2.921875 0.390625 2.515625 0.921875 C 2.265625 1.25 2.015625 1.5 1.5625 1.5 C 1.421875 1.5 1.140625 1.640625 1.03125 1.40625 C 0.953125 1.40625 1.203125 1.359375 1.34375 1.234375 C 1.453125 1.140625 1.59375 0.90625 1.59375 0.71875 C 1.59375 0.40625 1.15625 0.203125 1.0625 0.203125 C 0.828125 0.203125 0.3125 0.53125 0.3125 1.015625 C 0.3125 1.515625 0.9375 2.046875 1.5625 2.046875 C 2.578125 2.046875 3.78125 0.984375 4.0625 -0.15625 Z M 5.015625 -3.953125 "/>
</symbol>
<symbol overflow="visible" id="glyph0-4">
<path style="stroke:none;" d="M 3.015625 -3.15625 L 4.71875 -3.15625 C 6.125 -3.15625 7.6875 -4.34375 7.6875 -5.46875 C 7.6875 -6.234375 6.859375 -7.140625 5.546875 -7.140625 L 2.328125 -7.140625 C 2.140625 -7.140625 1.84375 -6.96875 1.84375 -6.78125 C 1.84375 -6.65625 2.109375 -6.5 2.3125 -6.5 C 2.4375 -6.5 2.625 -6.484375 2.734375 -6.484375 C 2.90625 -6.453125 2.78125 -6.59375 2.78125 -6.484375 C 2.78125 -6.4375 2.765625 -6.40625 2.734375 -6.296875 L 1.40625 -0.9375 C 1.3125 -0.546875 1.46875 -0.640625 0.671875 -0.640625 C 0.515625 -0.640625 0.21875 -0.46875 0.21875 -0.28125 C 0.21875 -0.15625 0.515625 0 0.546875 0 C 0.828125 0 1.53125 -0.03125 1.8125 -0.03125 C 2.03125 -0.03125 2.25 -0.015625 2.453125 -0.015625 C 2.671875 -0.015625 2.890625 0 3.09375 0 C 3.171875 0 3.46875 -0.15625 3.46875 -0.359375 C 3.46875 -0.46875 3.203125 -0.640625 3.015625 -0.640625 C 2.65625 -0.640625 2.546875 -0.46875 2.546875 -0.640625 C 2.546875 -0.703125 2.5625 -0.75 2.578125 -0.8125 L 3.15625 -3.15625 Z M 3.90625 -6.28125 C 4 -6.625 3.84375 -6.5 4.28125 -6.5 L 5.234375 -6.5 C 6.0625 -6.5 6.40625 -6.390625 6.40625 -5.703125 C 6.40625 -5.3125 6.265625 -4.578125 5.875 -4.21875 C 5.375 -3.765625 4.90625 -3.734375 4.46875 -3.734375 L 3.265625 -3.734375 Z M 3.90625 -6.28125 "/>
</symbol>
<symbol overflow="visible" id="glyph0-5">
<path style="stroke:none;" d="M 2.1875 -0.171875 C 2.1875 -0.828125 1.78125 -1.390625 1.390625 -1.390625 C 1.0625 -1.390625 0.671875 -0.96875 0.671875 -0.6875 C 0.671875 -0.421875 1.0625 0 1.390625 0 C 1.5 0 1.75 -0.09375 1.859375 -0.171875 C 1.890625 -0.203125 1.78125 -0.15625 1.78125 -0.15625 C 1.796875 -0.15625 1.625 -0.3125 1.625 -0.171875 C 1.625 0.5625 1.328125 1.046875 1 1.375 C 0.890625 1.484375 0.84375 1.625 0.84375 1.65625 C 0.84375 1.71875 1.0625 1.921875 1.109375 1.921875 C 1.21875 1.921875 2.1875 1 2.1875 -0.171875 Z M 2.1875 -0.171875 "/>
</symbol>
<symbol overflow="visible" id="glyph0-6">
<path style="stroke:none;" d="M 5.21875 -6.203125 C 5.078125 -6.078125 4.703125 -5.6875 4.703125 -5.5 C 4.703125 -5.40625 4.984375 -5.140625 5.078125 -5.140625 C 5.171875 -5.140625 5.34375 -5.265625 5.390625 -5.328125 C 5.515625 -5.46875 5.734375 -5.75 6.1875 -5.96875 C 6.25 -6.015625 6.40625 -6.171875 6.40625 -6.296875 C 6.40625 -6.390625 6.28125 -6.5625 6.203125 -6.609375 C 5.984375 -6.765625 5.9375 -6.8125 5.859375 -7.0625 C 5.828125 -7.140625 5.625 -7.453125 5.484375 -7.453125 C 5.34375 -7.453125 5.109375 -7.140625 5.109375 -7.0625 C 5.109375 -7.015625 5.234375 -6.59375 5.1875 -6.65625 L 2.15625 -6.65625 C 2 -6.65625 1.640625 -6.484375 1.640625 -6.296875 C 1.640625 -6.09375 2 -5.9375 2.15625 -5.9375 L 5.359375 -5.9375 Z M 5.21875 -6.203125 "/>
</symbol>
<symbol overflow="visible" id="glyph0-7">
<path style="stroke:none;" d="M 0.703125 -0.75 C 0.671875 -0.59375 0.609375 -0.375 0.609375 -0.3125 C 0.609375 -0.140625 0.921875 0.109375 1.078125 0.109375 C 1.203125 0.109375 1.546875 -0.125 1.59375 -0.28125 C 1.578125 -0.234375 1.75 -0.8125 1.796875 -1.0625 L 2.03125 -1.96875 C 2.078125 -2.1875 2.140625 -2.40625 2.1875 -2.625 C 2.234375 -2.796875 2.3125 -3.09375 2.328125 -3.125 C 2.46875 -3.4375 2.828125 -4.1875 3.78125 -4.1875 C 4.234375 -4.1875 4.140625 -3.984375 4.140625 -3.65625 C 4.140625 -3.03125 3.65625 -1.75 3.484375 -1.328125 C 3.40625 -1.09375 3.390625 -0.984375 3.390625 -0.875 C 3.390625 -0.40625 3.921875 0.109375 4.390625 0.109375 C 5.328125 0.109375 5.859375 -1.5 5.859375 -1.578125 C 5.859375 -1.6875 5.609375 -1.859375 5.578125 -1.859375 C 5.46875 -1.859375 5.296875 -1.65625 5.25 -1.5 C 5.046875 -0.828125 4.890625 -0.4375 4.40625 -0.4375 C 4.234375 -0.4375 4.34375 -0.375 4.34375 -0.59375 C 4.34375 -0.84375 4.421875 -1.09375 4.515625 -1.3125 C 4.703125 -1.828125 5.125 -2.9375 5.125 -3.5 C 5.125 -4.171875 4.53125 -4.734375 3.8125 -4.734375 C 2.90625 -4.734375 2.296875 -4.046875 2.125 -3.8125 L 2.421875 -3.703125 C 2.375 -4.25 1.796875 -4.734375 1.328125 -4.734375 C 0.875 -4.734375 0.5625 -4.296875 0.484375 -4.171875 C 0.25 -3.65625 0.109375 -3.078125 0.109375 -3.03125 C 0.109375 -2.9375 0.390625 -2.765625 0.40625 -2.765625 C 0.515625 -2.765625 0.6875 -2.9375 0.75 -3.15625 C 0.921875 -3.875 0.953125 -4.1875 1.3125 -4.1875 C 1.5 -4.1875 1.4375 -4.21875 1.4375 -3.890625 C 1.4375 -3.671875 1.40625 -3.5625 1.28125 -3.046875 Z M 0.703125 -0.75 "/>
</symbol>
<symbol overflow="visible" id="glyph1-0">
<path style="stroke:none;" d=""/>
</symbol>
<symbol overflow="visible" id="glyph1-1">
<path style="stroke:none;" d="M 6.84375 -3.265625 C 7 -3.265625 7.359375 -3.421875 7.359375 -3.625 C 7.359375 -3.8125 7 -3.984375 6.859375 -3.984375 L 0.890625 -3.984375 C 0.75 -3.984375 0.375 -3.8125 0.375 -3.625 C 0.375 -3.421875 0.75 -3.265625 0.890625 -3.265625 Z M 6.859375 -1.328125 C 7 -1.328125 7.359375 -1.484375 7.359375 -1.6875 C 7.359375 -1.890625 7 -2.046875 6.84375 -2.046875 L 0.890625 -2.046875 C 0.75 -2.046875 0.375 -1.890625 0.375 -1.6875 C 0.375 -1.484375 0.75 -1.328125 0.890625 -1.328125 Z M 6.859375 -1.328125 "/>
</symbol>
<symbol overflow="visible" id="glyph1-2">
<path style="stroke:none;" d="M 3.46875 2.234375 C 3.46875 2.203125 3.421875 2.0625 3.25 1.890625 C 2 0.640625 1.734375 -1.125 1.734375 -2.65625 C 1.734375 -4.390625 2.0625 -6.015625 3.296875 -7.25 C 3.421875 -7.375 3.46875 -7.5 3.46875 -7.53125 C 3.46875 -7.609375 3.265625 -7.8125 3.203125 -7.8125 C 3.09375 -7.8125 2.03125 -6.953125 1.4375 -5.6875 C 0.921875 -4.59375 0.8125 -3.484375 0.8125 -2.65625 C 0.8125 -1.875 0.921875 -0.671875 1.46875 0.453125 C 2.0625 1.6875 3.09375 2.5 3.203125 2.5 C 3.265625 2.5 3.46875 2.296875 3.46875 2.234375 Z M 3.46875 2.234375 "/>
</symbol>
<symbol overflow="visible" id="glyph1-3">
<path style="stroke:none;" d="M 3.09375 -6.546875 C 3.09375 -6.78125 2.9375 -6.96875 2.625 -6.96875 C 1.953125 -6.28125 1.203125 -6.328125 0.703125 -6.328125 L 0.703125 -5.6875 C 1.09375 -5.6875 1.796875 -5.734375 2.015625 -5.859375 L 2.015625 -0.953125 C 2.015625 -0.59375 2.15625 -0.640625 1.265625 -0.640625 L 0.765625 -0.640625 L 0.765625 0.015625 C 1.296875 -0.03125 2.15625 -0.03125 2.5625 -0.03125 C 2.953125 -0.03125 3.828125 -0.03125 4.34375 0.015625 L 4.34375 -0.640625 L 3.859375 -0.640625 C 2.953125 -0.640625 3.09375 -0.578125 3.09375 -0.953125 Z M 3.09375 -6.546875 "/>
</symbol>
<symbol overflow="visible" id="glyph1-4">
<path style="stroke:none;" d="M 3.046875 -2.65625 C 3.046875 -3.421875 2.9375 -4.640625 2.390625 -5.765625 C 1.796875 -6.984375 0.765625 -7.8125 0.671875 -7.8125 C 0.609375 -7.8125 0.390625 -7.59375 0.390625 -7.53125 C 0.390625 -7.5 0.4375 -7.375 0.625 -7.203125 C 1.609375 -6.203125 2.125 -4.734375 2.125 -2.65625 C 2.125 -0.953125 1.796875 0.6875 0.5625 1.9375 C 0.4375 2.0625 0.390625 2.203125 0.390625 2.234375 C 0.390625 2.296875 0.609375 2.5 0.671875 2.5 C 0.765625 2.5 1.828125 1.65625 2.421875 0.390625 C 2.9375 -0.703125 3.046875 -1.8125 3.046875 -2.65625 Z M 3.046875 -2.65625 "/>
</symbol>
<symbol overflow="visible" id="glyph2-0">
<path style="stroke:none;" d=""/>
</symbol>
<symbol overflow="visible" id="glyph2-1">
<path style="stroke:none;" d="M 6.5625 -2.296875 C 6.734375 -2.296875 7.125 -2.421875 7.125 -2.625 C 7.125 -2.828125 6.734375 -2.953125 6.5625 -2.953125 L 1.171875 -2.953125 C 1 -2.953125 0.625 -2.828125 0.625 -2.625 C 0.625 -2.421875 1 -2.296875 1.171875 -2.296875 Z M 6.5625 -2.296875 "/>
</symbol>
</g>
</defs>
<g id="surface1">
<path style="fill:none;stroke-width:0.99628;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-miterlimit:10;" d="M 90.710813 -0.000375 C 90.710813 50.097281 50.097531 90.710562 -0.000125 90.710562 C -50.097781 90.710562 -90.711062 50.097281 -90.711062 -0.000375 C -90.711062 -50.098031 -50.097781 -90.711313 -0.000125 -90.711313 C 50.097531 -90.711313 90.710813 -50.098031 90.710813 -0.000375 Z M 90.710813 -0.000375 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L -11.179812 136.218375 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L 127.792844 -77.488656 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L -11.179812 136.218375 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -7.652719 L 127.792844 -56.933969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L -11.179812 136.218375 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 12.901969 L 127.792844 -36.383188 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L -11.179812 136.218375 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 33.45275 L 127.792844 -15.8285 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L -11.179812 136.218375 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 54.007437 L 127.792844 4.722281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L -11.179812 136.218375 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 74.558219 L 127.792844 25.276969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L -11.179812 136.218375 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 95.112906 L 127.792844 45.82775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L -11.179812 136.218375 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 115.663687 L 127.792844 66.382437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L -11.179812 136.218375 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 136.218375 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 6.191281 -34.363656 L 6.191281 130.058219 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L 127.792844 -77.488656 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 6.191281 -34.363656 L 6.191281 130.058219 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -7.652719 L 127.792844 -56.933969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 6.191281 -34.363656 L 6.191281 130.058219 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 12.901969 L 127.792844 -36.383188 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 6.191281 -34.363656 L 6.191281 130.058219 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 33.45275 L 127.792844 -15.8285 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 6.191281 -34.363656 L 6.191281 130.058219 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 54.007437 L 127.792844 4.722281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 6.191281 -34.363656 L 6.191281 130.058219 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 74.558219 L 127.792844 25.276969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 6.191281 -34.363656 L 6.191281 130.058219 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 95.112906 L 127.792844 45.82775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 6.191281 -34.363656 L 6.191281 130.058219 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 115.663687 L 127.792844 66.382437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 6.191281 -34.363656 L 6.191281 130.058219 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 136.218375 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 23.562375 -40.523813 L 23.562375 123.898062 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L 127.792844 -77.488656 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 23.562375 -40.523813 L 23.562375 123.898062 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -7.652719 L 127.792844 -56.933969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 23.562375 -40.523813 L 23.562375 123.898062 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 12.901969 L 127.792844 -36.383188 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 23.562375 -40.523813 L 23.562375 123.898062 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 33.45275 L 127.792844 -15.8285 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 23.562375 -40.523813 L 23.562375 123.898062 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 54.007437 L 127.792844 4.722281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 23.562375 -40.523813 L 23.562375 123.898062 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 74.558219 L 127.792844 25.276969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 23.562375 -40.523813 L 23.562375 123.898062 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 95.112906 L 127.792844 45.82775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 23.562375 -40.523813 L 23.562375 123.898062 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 115.663687 L 127.792844 66.382437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 23.562375 -40.523813 L 23.562375 123.898062 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 136.218375 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 40.937375 -46.683969 L 40.937375 117.737906 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L 127.792844 -77.488656 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 40.937375 -46.683969 L 40.937375 117.737906 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -7.652719 L 127.792844 -56.933969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 40.937375 -46.683969 L 40.937375 117.737906 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 12.901969 L 127.792844 -36.383188 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 40.937375 -46.683969 L 40.937375 117.737906 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 33.45275 L 127.792844 -15.8285 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 40.937375 -46.683969 L 40.937375 117.737906 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 54.007437 L 127.792844 4.722281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 40.937375 -46.683969 L 40.937375 117.737906 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 74.558219 L 127.792844 25.276969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 40.937375 -46.683969 L 40.937375 117.737906 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 95.112906 L 127.792844 45.82775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 40.937375 -46.683969 L 40.937375 117.737906 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 115.663687 L 127.792844 66.382437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 40.937375 -46.683969 L 40.937375 117.737906 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 136.218375 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 58.308469 -52.844125 L 58.308469 111.57775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L 127.792844 -77.488656 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 58.308469 -52.844125 L 58.308469 111.57775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -7.652719 L 127.792844 -56.933969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 58.308469 -52.844125 L 58.308469 111.57775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 12.901969 L 127.792844 -36.383188 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 58.308469 -52.844125 L 58.308469 111.57775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 33.45275 L 127.792844 -15.8285 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 58.308469 -52.844125 L 58.308469 111.57775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 54.007437 L 127.792844 4.722281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 58.308469 -52.844125 L 58.308469 111.57775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 74.558219 L 127.792844 25.276969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 58.308469 -52.844125 L 58.308469 111.57775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 95.112906 L 127.792844 45.82775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 58.308469 -52.844125 L 58.308469 111.57775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 115.663687 L 127.792844 66.382437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 58.308469 -52.844125 L 58.308469 111.57775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 136.218375 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 75.679563 -59.004281 L 75.679563 105.417594 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L 127.792844 -77.488656 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 75.679563 -59.004281 L 75.679563 105.417594 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -7.652719 L 127.792844 -56.933969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 75.679563 -59.004281 L 75.679563 105.417594 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 12.901969 L 127.792844 -36.383188 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 75.679563 -59.004281 L 75.679563 105.417594 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 33.45275 L 127.792844 -15.8285 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 75.679563 -59.004281 L 75.679563 105.417594 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 54.007437 L 127.792844 4.722281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 75.679563 -59.004281 L 75.679563 105.417594 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 74.558219 L 127.792844 25.276969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 75.679563 -59.004281 L 75.679563 105.417594 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 95.112906 L 127.792844 45.82775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 75.679563 -59.004281 L 75.679563 105.417594 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 115.663687 L 127.792844 66.382437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 75.679563 -59.004281 L 75.679563 105.417594 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 136.218375 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 93.050656 -65.168344 L 93.050656 99.257437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L 127.792844 -77.488656 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 93.050656 -65.168344 L 93.050656 99.257437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -7.652719 L 127.792844 -56.933969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 93.050656 -65.168344 L 93.050656 99.257437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 12.901969 L 127.792844 -36.383188 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 93.050656 -65.168344 L 93.050656 99.257437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 33.45275 L 127.792844 -15.8285 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 93.050656 -65.168344 L 93.050656 99.257437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 54.007437 L 127.792844 4.722281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 93.050656 -65.168344 L 93.050656 99.257437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 74.558219 L 127.792844 25.276969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 93.050656 -65.168344 L 93.050656 99.257437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 95.112906 L 127.792844 45.82775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 93.050656 -65.168344 L 93.050656 99.257437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 115.663687 L 127.792844 66.382437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 93.050656 -65.168344 L 93.050656 99.257437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 136.218375 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 110.42175 -71.3285 L 110.42175 93.097281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L 127.792844 -77.488656 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 110.42175 -71.3285 L 110.42175 93.097281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -7.652719 L 127.792844 -56.933969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 110.42175 -71.3285 L 110.42175 93.097281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 12.901969 L 127.792844 -36.383188 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 110.42175 -71.3285 L 110.42175 93.097281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 33.45275 L 127.792844 -15.8285 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 110.42175 -71.3285 L 110.42175 93.097281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 54.007437 L 127.792844 4.722281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 110.42175 -71.3285 L 110.42175 93.097281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 74.558219 L 127.792844 25.276969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 110.42175 -71.3285 L 110.42175 93.097281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 95.112906 L 127.792844 45.82775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 110.42175 -71.3285 L 110.42175 93.097281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 115.663687 L 127.792844 66.382437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 110.42175 -71.3285 L 110.42175 93.097281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 136.218375 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 127.792844 -77.488656 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -28.2035 L 127.792844 -77.488656 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 127.792844 -77.488656 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 -7.652719 L 127.792844 -56.933969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 127.792844 -77.488656 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 12.901969 L 127.792844 -36.383188 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 127.792844 -77.488656 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 33.45275 L 127.792844 -15.8285 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 127.792844 -77.488656 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 54.007437 L 127.792844 4.722281 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 127.792844 -77.488656 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 74.558219 L 127.792844 25.276969 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 127.792844 -77.488656 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 95.112906 L 127.792844 45.82775 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 127.792844 -77.488656 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 115.663687 L 127.792844 66.382437 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M 127.792844 -77.488656 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(50%,50%,50%);stroke-opacity:1;stroke-miterlimit:10;" d="M -11.179812 136.218375 L 127.792844 86.937125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-dasharray:2.98883,2.98883;stroke-miterlimit:10;" d="M -0.000125 82.198844 C -32.199344 65.984 -58.297 16.038687 -58.297 -29.35975 C -58.297 -74.758188 -32.199344 -98.414438 -0.000125 -82.199594 C 32.199094 -65.98475 58.300656 -16.035531 58.300656 29.362906 C 58.300656 74.757437 32.199094 98.413687 -0.000125 82.198844 Z M -0.000125 82.198844 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-dasharray:2.98883,2.98883;stroke-miterlimit:10;" d="M -0.000125 -82.199594 L -0.000125 -0.000375 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-dasharray:2.98883,2.98883;stroke-miterlimit:10;" d="M -58.297 -29.35975 C -19.925906 -42.969125 37.277219 -40.851938 69.476438 -24.637094 C 101.675656 -8.42225 96.67175 15.753531 58.300656 29.362906 C 19.925656 42.968375 -37.277469 40.855094 -69.476687 24.636344 C -101.675906 8.4215 -96.672 -15.754281 -58.297 -29.35975 Z M -58.297 -29.35975 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.3985;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-dasharray:2.98883,2.98883;stroke-miterlimit:10;" d="M -69.476687 24.636344 L -0.000125 -0.000375 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.99628;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-miterlimit:10;" d="M -0.000125 -0.000375 L -101.293094 -51.016 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.79701;stroke-linecap:round;stroke-linejoin:round;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-miterlimit:10;" d="M -1.733041 2.312551 C -1.588808 1.443861 0.000716229 0.144706 0.435307 0.000190282 C -0.000119172 -0.143551 -1.586695 -1.443983 -1.734209 -2.310081 " transform="matrix(-0.89308,0.44978,0.44978,0.89308,104.87696,280.24935)"/>
<g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
  <use xlink:href="#glyph0-1" x="95.244" y="282.768"/>
</g>
<path style="fill:none;stroke-width:0.99628;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-miterlimit:10;" d="M -0.000125 -0.000375 L 120.816281 -42.844125 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.79701;stroke-linecap:round;stroke-linejoin:round;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-miterlimit:10;" d="M -1.733632 2.311894 C -1.587384 1.443622 0.000261312 0.14562 0.432986 0.000644782 C -0.000393037 -0.144744 -1.590481 -1.446358 -1.735902 -2.310294 " transform="matrix(0.94246,0.3342,0.3342,-0.94246,326.99015,272.07856)"/>
<g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
  <use xlink:href="#glyph0-2" x="331.593" y="274.501"/>
</g>
<path style="fill:none;stroke-width:0.99628;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-miterlimit:10;" d="M -0.000125 -0.000375 L -0.000125 143.038687 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.79701;stroke-linecap:round;stroke-linejoin:round;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-miterlimit:10;" d="M -1.733358 2.312625 C -1.588826 1.445437 0.0010175 0.144656 0.434611 0.000125 C 0.0010175 -0.144406 -1.588826 -1.445188 -1.733358 -2.312375 " transform="matrix(0,-1,-1,0,206.172,86.19633)"/>
<g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
  <use xlink:href="#glyph0-3" x="203.551" y="79.609"/>
</g>
<path style="fill:none;stroke-width:0.99628;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-dasharray:2.98883,2.98883;stroke-miterlimit:10;" d="M -0.000125 -0.000375 L 58.308469 29.366812 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill-rule:nonzero;fill:rgb(0%,0%,0%);fill-opacity:1;stroke-width:0.79701;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-miterlimit:10;" d="M 60.218625 29.366812 C 60.218625 30.4215 59.363156 31.276969 58.308469 31.276969 C 57.249875 31.276969 56.394406 30.4215 56.394406 29.366812 C 56.394406 28.308219 57.249875 27.45275 58.308469 27.45275 C 59.363156 27.45275 60.218625 28.308219 60.218625 29.366812 Z M 60.218625 29.366812 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill-rule:nonzero;fill:rgb(0%,0%,0%);fill-opacity:1;stroke-width:0.79701;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-miterlimit:10;" d="M 1.913938 -0.000375 C 1.913938 1.058219 1.054563 1.913687 -0.000125 1.913687 C -1.054812 1.913687 -1.914187 1.058219 -1.914187 -0.000375 C -1.914187 -1.055063 -1.054812 -1.914438 -0.000125 -1.914438 C 1.054563 -1.914438 1.913938 -1.055063 1.913938 -0.000375 Z M 1.913938 -0.000375 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill-rule:nonzero;fill:rgb(0%,0%,0%);fill-opacity:1;stroke-width:0.79701;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-miterlimit:10;" d="M 1.913938 82.210562 C 1.913938 83.269156 1.054563 84.124625 -0.000125 84.124625 C -1.054812 84.124625 -1.914187 83.269156 -1.914187 82.210562 C -1.914187 81.155875 -1.054812 80.2965 -0.000125 80.2965 C 1.054563 80.2965 1.913938 81.155875 1.913938 82.210562 Z M 1.913938 82.210562 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill-rule:nonzero;fill:rgb(0%,0%,0%);fill-opacity:1;stroke-width:0.79701;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-miterlimit:10;" d="M 71.398313 -24.641 C 71.398313 -23.586313 70.542844 -22.726938 69.488156 -22.726938 C 68.429563 -22.726938 67.574094 -23.586313 67.574094 -24.641 C 67.574094 -25.699594 68.429563 -26.555063 69.488156 -26.555063 C 70.542844 -26.555063 71.398313 -25.699594 71.398313 -24.641 Z M 71.398313 -24.641 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill-rule:nonzero;fill:rgb(0%,0%,0%);fill-opacity:1;stroke-width:0.79701;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-miterlimit:10;" d="M -56.394656 -29.363656 C -56.394656 -28.308969 -57.250125 -27.4535 -58.308719 -27.4535 C -59.363406 -27.4535 -60.218875 -28.308969 -60.218875 -29.363656 C -60.218875 -30.42225 -59.363406 -31.277719 -58.308719 -31.277719 C -57.250125 -31.277719 -56.394656 -30.42225 -56.394656 -29.363656 Z M -56.394656 -29.363656 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill-rule:nonzero;fill:rgb(0%,0%,0%);fill-opacity:1;stroke-width:0.79701;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-miterlimit:10;" d="M 122.781125 15.413687 C 122.781125 16.468375 121.925656 17.323844 120.867063 17.323844 C 119.812375 17.323844 118.956906 16.468375 118.956906 15.413687 C 118.956906 14.355094 119.812375 13.499625 120.867063 13.499625 C 121.925656 13.499625 122.781125 14.355094 122.781125 15.413687 Z M 122.781125 15.413687 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill-rule:nonzero;fill:rgb(100%,0%,0%);fill-opacity:1;stroke-width:0.79701;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(100%,0%,0%);stroke-opacity:1;stroke-miterlimit:10;" d="M 89.370969 11.148062 C 89.370969 12.20275 88.5155 13.062125 87.456906 13.062125 C 86.402219 13.062125 85.54675 12.20275 85.54675 11.148062 C 85.54675 10.093375 86.402219 9.234 87.456906 9.234 C 88.5155 9.234 89.370969 10.093375 89.370969 11.148062 Z M 89.370969 11.148062 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.99628;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(100%,0%,0%);stroke-opacity:1;stroke-dasharray:2.98883,2.98883;stroke-miterlimit:10;" d="M -0.000125 -0.000375 L 120.867063 15.413687 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
  <use xlink:href="#glyph0-4" x="330.859" y="207.512"/>
</g>
<g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
  <use xlink:href="#glyph1-1" x="341.407" y="207.512"/>
</g>
<g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
  <use xlink:href="#glyph1-2" x="351.91555" y="207.512"/>
</g>
<g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
  <use xlink:href="#glyph0-2" x="355.797" y="207.512"/>
  <use xlink:href="#glyph0-5" x="361.490626" y="207.512"/>
</g>
<g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
  <use xlink:href="#glyph0-3" x="365.912028" y="207.512"/>
</g>
<g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
  <use xlink:href="#glyph0-5" x="371.155344" y="207.512"/>
</g>
<g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
  <use xlink:href="#glyph2-1" x="375.589" y="207.512"/>
</g>
<g style="fill:rgb(0%,0%,0%);fill-opacity:1;">
  <use xlink:href="#glyph1-3" x="383.337" y="207.512"/>
  <use xlink:href="#glyph1-4" x="388.3183" y="207.512"/>
</g>
<path style="fill:none;stroke-width:0.99628;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,100%);stroke-opacity:1;stroke-miterlimit:10;" d="M 120.867063 15.413687 L 98.285031 4.038687 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
<path style="fill:none;stroke-width:0.79701;stroke-linecap:round;stroke-linejoin:round;stroke:rgb(0%,0%,100%);stroke-opacity:1;stroke-miterlimit:10;" d="M -1.732077 2.311386 C -1.587845 1.442695 0.00168001 0.14354 0.432782 0.000781806 C 0.000844605 -0.144717 -1.589221 -1.443392 -1.733245 -2.311247 " transform="matrix(-0.89308,0.44978,0.44978,0.89308,304.45647,225.19527)"/>
<g style="fill:rgb(0%,0%,100%);fill-opacity:1;">
  <use xlink:href="#glyph0-6" x="307.266" y="236.506"/>
</g>
<g style="fill:rgb(0%,0%,100%);fill-opacity:1;">
  <use xlink:href="#glyph0-7" x="307.53499" y="236.506"/>
</g>
<path style="fill:none;stroke-width:0.99628;stroke-linecap:butt;stroke-linejoin:miter;stroke:rgb(0%,0%,0%);stroke-opacity:1;stroke-miterlimit:10;" d="M 106.785031 13.616812 C 106.988156 12.023062 107.464719 10.472281 108.187375 9.034781 " transform="matrix(1,0,0,-1,206.172,229.234)"/>
</g>
</svg>
</center>
</div>

设原点为 $O$, 考虑正方形上的一点 $P=(x,y,1)$, 
$P$处的面积微元为 $\mathrm{d}A = \mathrm{d}x\cdot\mathrm{d}y$, 法线方向为 $\vec{n} = (0,0,1)$, 
$P$点到原点的距离为 $R = |OP| = \sqrt{x^2+y^2+1}$, $\vec{PO}$ 方向的单位向量为 $\vec{p} = \dfrac{(x,y,1)}{R}$, 
$\mathrm{d}A$ 在 $\vec{PO}$ 方向上的投影面积为 $\mathrm{d}A\cdot\cos\angle(\vec{n},\vec{p})$, 该投影面积对应的球半径为 $R$, 所以对于 $x\in[x_1,x_2], y\in[y_1,y_2]$的一块矩形区域对应立体角为:
$$
\begin{aligned} 
\Omega_{[x_1,x_2]\times[y_1,y_2]} &= \int_A\frac{(\vec{n}\cdot\vec{p})}{R^2} \ \mathrm{d}A = \int_A\frac{1}{R^3} \ \mathrm{d}A\\\ 
&= \int_{y_1}^{y_2}{\int_{x_1}^{x_2}\frac{1}{(x^2+y^2+1)^{\frac{3}{2}}}\ \mathrm{d}x}\ \mathrm{d}y \ .
\end{aligned} 
$$
先计算 
$$
f(s,t) = \Omega_{[0,s]\times[0,t]} = \int_0^t{\int_0^s\frac{1}{(x^2+y^2+1)^{\frac{3}{2}}}\ \mathrm{d}x}\ \mathrm{d}y\ , 
$$
令 $u = \dfrac{x}{\sqrt{x^2+y^2+1}}$, 则积分上下限分别是 $u(x=0) = 0$, $u(x=s)=\dfrac{s}{\sqrt{s^2+y^2+1}}$, 且
$$\dfrac{\mathrm{d}u}{\mathrm{d}x} = \dfrac{y^2+1}{(x^2+y^2+1)^\frac{3}{2}} ,$$ 
积分换元得:
$$
\begin{aligned} 
f(s,t) &= \int_0^t{\int_0^{\frac{s}{\sqrt{s^2+y^2+1}}}{\frac{1}{1+y^2}}\ \mathrm{d}u}\ \mathrm{d}y\\\ 
&=\int_0^t{\frac{s}{(y^2+1)\sqrt{y^2+s^2+1}}}\ \mathrm{d}y . 
\end{aligned} 
$$
继续换元, 令 $v = \dfrac{y}{\sqrt{y^2+s^2+1}} $, 积分上下限为 $v(y=0) = 0$, $v(y=t) = \dfrac{t}{\sqrt{s^2+t^2+1}}$, 并且
$$
\begin{aligned} 
\frac{\mathrm{d}v}{\mathrm{d}y} &= \frac{s^2+1}{(y^2+s^2+1)^\frac{3}{2}} ,\\\ 
y^2 + 1 &= \frac{v^2s^2+1}{1-v^2} ,\\\ 
1-v^2&=\frac{s^2+1}{y^2+s^2+1} .
\end{aligned} 
$$
于是
$$
\begin{aligned} 
f(s,t) &= \int_0^\frac{t}{\sqrt{s^2+t^2+1}} {\frac{s(1-v^2)}{v^2s^2+1}\cdot\frac{y^2+s^2+1}{s^2+1}}\ \mathrm{d}v \\\ 
&= \int_0^\frac{t}{\sqrt{s^2+t^2+1}}{\frac{s}{s^2v^2+1}}\ \mathrm{d}v\\\ 
&= \int_0^\frac{t}{\sqrt{s^2+t^2+1}}{\frac{1}{s}\cdot\frac{1}{v^2+\dfrac{1}{s^2}}}\ \mathrm{d}v\\\ 
&= \frac{1}{s}\cdot s\arctan(sv)\bigg|_{v=0}^{v=\frac{t}{\sqrt{s^2+t^2+1}}}\\\ 
&= \arctan(\frac{st}{\sqrt{s^2+t^2+1}}) .
\end{aligned} 
$$

得到 $f(s,t)$ 的表达式之后, 可以用下面的方法计算其他(任意矩形)范围的立体角:
$$\Omega_{[x_1,x_2]\times[y_1,y_2]} = f(x_2,y_2) - f(x_1,y_2) - f(x_2,y_1) + f(x_1,y_1) .$$

作为验证, 考虑 cubemap 的一个面, 占据了 $\dfrac{1}{6}$ 个球面, 对应的立体角应该是 $\dfrac{2\pi}{3}$. 而
$$
\begin{aligned}
\Omega_{[-1,1]\times[-1,1]} &= f(1,1) - f(-1,1) - f(1,-1) + f(1,1) \\\ 
& = 4\times f(1,1) \\\ 
&= 4\times \arctan(\dfrac{1}{\sqrt{3}}) \\\ 
& = \dfrac{2\pi}{3} .
\end{aligned} 
$$

