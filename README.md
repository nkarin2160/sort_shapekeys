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
0:ベース  
1:eyeBlinkLeft  
2:eyeLookDownLeft  
3:eyeLookInLeft  
4:eyeLookOutLeft  
5:eyeLookUpLeft  
6:eyeSquintLeft  
7:eyeWideLeft  
8:eyeBlinkRight  
9:eyeLookDownRight  
10:eyeLookInRight  
11:eyeLookOutRight  
12:eyeLookUpRight  
13:eyeSquintRight  
14:eyeWideRight  
15:jawForward  
16:jawLeft  
17:jawRight  
18:jawOpen  
19:mouthClose  
20:mouthFunnel  
21:mouthPucker  
22:mouthLeft  
23:mouthRight  
24:mouthSmileLeft  
25:mouthSmileRight  
26:mouthFrownLeft  
27:mouthFrownRight  
28:mouthDimpleLeft  
29:mouthDimpleRight  
30:mouthStretchLeft  
31:mouthStretchRight  
32:mouthRollLower  
33:mouthRollUpper  
34:mouthShrugLower  
35:mouthShrugUpper  
36:mouthPressLeft  
37:mouthPressRight  
38:mouthLowerDownLeft  
39:mouthLowerDownRight  
40:mouthUpperUpLeft  
41:mouthUpperUpRight  
42:browDownLeft  
43:browDownRight  
44:browInnerUp  
45:browOuterUpLeft  
46:browOuterUpRight  
47:cheekPuff  
48:cheekSquintLeft  
49:cheekSquintRight  
50:noseSneerLeft  
51:noseSneerRight  
52:tongueOut  
53:headYaw  
54:headPitch  
55:headRoll  
56:leftEyeYaw  
57:leftEyePitch  
58:leftEyeRoll  
59:rightEyeYaw  
60:rightEyePitch  
61:rightEyeRoll  
### iFacialMocap  
0：ベース  
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
