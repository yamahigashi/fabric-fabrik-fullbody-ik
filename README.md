# FFFBIK: Fabric splice FABRIK FullBody IK
FFFBIK is Fabric Splice tool for full-body IK system, using extended FABRIK 
(Forward And Backward Reaching Inverse Kinematics), based-off a paper written by Andreas Aristidou(2014). Using Fabric Engine 1.15.0, works in many DCC's.

The main purposes of this project is studying Fabric Engine's KL language with building
 custom IK system using FABRIK algorithm, sharing experience with these concept, and leading to providing more
 effcient and flexible rigging solution.

## Description
Now implemented:
- the Fabric operator.
- Simple IK solver which has one end effector .
- Closed-loop chain solver that connects other solvers.
- Resolver that manages solvers execution order.
- Component that represent body parts. (arm, leg and ...)
 

## Demo
![](https://raw.githubusercontent.com/yamahigashi/fabric-fabrik-fullbody-ik/gh-pages/images/wip_fffbik2.gif)

## Requirement
Tested on Fabric Engine 1.15.0 which can be found ([Fabric engine (Get Fabric)](http://fabricengine.com/get-fabric/))

## Install
Simply clone this repository and add the 'Ext' folder to the 'FABRIC_EXTS_PATH' env variable.

## Usage
see Tests/testFFFBIK.kl and Tests/DCCSetupScripts/Softimage



## References
- Dr Andreas Aristidou [FABRIK](http://www.andreasaristidou.com/FABRIK.html) Research page
- Youtube video [Extending FABRIK with model constraints](https://www.youtube.com/watch?v=wjn19jBzJCE)

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)
