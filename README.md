2021/9/12 
変更  
1.authorの追記と修正  
"Original author": "gogo",  
"Edited by": "nkarin",    
2.ソートスロット名称、「FaceCap」を「LiveLink」に変更、及びその名称を利用するメソッドの名称もすべて置き換え。   
3.ソート名称をLiveLinkでそのまま使用できる名称に変更　※出典「https://jumpjun.net/bue4vtuber1/#toc7」  
4.「Basis」を「ベース」に変更  


# Blender Add-on: Sort Shapekeys
FaceCap用にBlender上でシェイプキーを並べ替えるスクリプトです。[DLはこちら](https://github.com/nkarin2160/sort_shapekeys/releases/download/v1.0/sort_shapekeys.zip)    
<br>
![アドオン画像](./doc/sort_shapekeys_00.jpg)

## 機能一覧_Functions  
### Type  
FaceCap/iFacialMocapを選択します。  
以降のCheck, Create Missings, Sortはここで選択したTypeに従って処理します。  

### Check  
選択しているオブジェクトにTypeのシェイプキーがすべて存在するかをチェックします。  
存在しなかったシェイプキー名をinfoに表示します。  

### Create Missings  
選択しているオブジェクトにTypeのシェイプキーがすべて存在するかをチェックし、  
存在しなかったシェイプキーを空シェイプキーとして作成します。  

### Sort  
選択しているオブジェクトのシェイプキーをTypeに従ってsortします。  
Typeのシェイプキーすべてが揃っていない場合、この操作はキャンセルされます。  

## Shapekeyのsort順  
### LiveLink 
0:eyeBlinkLeft  
1:eyeLookDownLeft  
2:eyeLookInLeft  
3:eyeLookOutLeft  
4:eyeLookUpLeft  
5:eyeSquintLeft  
6:eyeWideLeft  
7:eyeBlinkRight  
8:eyeLookDownRight  
9:eyeLookInRight  
10:eyeLookOutRight  
11:eyeLookUpRight  
12:eyeSquintRight  
13:eyeWideRight  
14:jawForward  
15:jawLeft  
16:jawRight  
17:jawOpen  
18:mouthClose  
19:mouthFunnel  
20:mouthPucker  
21:mouthLeft  
22:mouthRight  
23:mouthSmileLeft  
24:mouthSmileRight  
25:mouthFrownLeft  
26:mouthFrownRight  
27:mouthDimpleLeft  
28:mouthDimpleRight  
29:mouthStretchLeft  
30:mouthStretchRight  
31:mouthRollLower  
32:mouthRollUpper  
33:mouthShrugLower  
34:mouthShrugUpper  
35:mouthPressLeft  
36:mouthPressRight  
37:mouthLowerDownLeft  
38:mouthLowerDownRight  
39:mouthUpperUpLeft  
40:mouthUpperUpRight  
41:browDownLeft  
42:browDownRight  
43:browInnerUp  
44:browOuterUpLeft  
45:browOuterUpRight  
46:cheekPuff  
47:cheekSquintLeft  
48:cheekSquintRight  
49:noseSneerLeft  
50:noseSneerRight  
51:tongueOut  
52:headYaw  
53:headPitch  
54:headRoll  
55:leftEyeYaw  
56:leftEyePitch  
57:leftEyeRoll  
58:rightEyeYaw  
59:rightEyePitch  
60:rightEyeRoll   
### iFacialMocap  
0：Basis  
1：browInnerUp  
2：browDownLeft  
3：browDownRight  
4：browOuterUpLeft  
5：browOuterUpRight  
6：eyeLookUpLeft  
7：eyeLookUpRight  
8：eyeLookDownLeft  
9：eyeLookDownRight  
10：eyeLookInLeft  
11：eyeLookInRight  
12：eyeLookOutLeft  
13：eyeLookOutRight  
14：eyeBlinkLeft  
15：eyeBlinkRight  
16：eyeSquintLeft  
17：eyeSquintRight  
18：eyeWideLeft  
19：eyeWideRight  
20：cheekPuff  
21：cheekSquintLeft  
22：cheekSquintRight  
23：noseSneerLeft  
24：noseSneerRight  
25：jawOpen  
26：jawForward  
27：jawLeft  
28：jawRight  
29：mouthFunnel  
30：mouthPucker  
31：mouthLeft  
32：mouthRight  
33：mouthRollUpper  
34：mouthRollLower  
35：mouthShrugUpper  
36：mouthShrugLower  
37：mouthClose  
38：mouthSmileLeft  
39：mouthSmileRight  
40：mouthFrownLeft  
41：mouthFrownRight  
42：mouthDimpleLeft  
43：mouthDimpleRight  
44：mouthUpperUpLeft  
45：mouthUpperUpRight  
46：mouthLowerDownLeft  
47：mouthLowerDownRight  
48：mouthPressLeft  
49：mouthPressRight  
50：mouthStretchLeft  
51：mouthStretchRight  
52：tongueOut  
