
# CHANGE THIS
JSONFilePath = r"D:\fabric\Exts\FFFBIK\Tests\DCCSetupScripts\Softimage\sample_si.canvas"


import os
if not os.path.exists(JSONFilePath):
    raise "CHANGE JSONFilePath"

Application.GetPrim("Null", "", "", "")
Application.GetPrim("Null", "l_hand_ik", "", "")
Application.GetPrim("Null", "l_hand_upv", "", "")
Application.GetPrim("Null", "r_hand_ik", "", "")
Application.GetPrim("Null", "r_hand_upv", "", "")

Application.GetPrim("Null", "l_foot_ik", "", "")
Application.GetPrim("Null", "l_foot_upv", "", "")
Application.GetPrim("Null", "r_foot_ik", "", "")
Application.GetPrim("Null", "r_foot_upv", "", "")

Application.SetValue("l_hand_upv.null.primary_icon", 2, "")
Application.SetValue("l_hand_upv.null.size", 0.3, "")
Application.SetValue("r_hand_upv.null.primary_icon", 2, "")
Application.SetValue("r_hand_upv.null.size", 0.3, "")

Application.SetValue("l_foot_upv.null.primary_icon", 2, "")
Application.SetValue("l_foot_upv.null.size", 0.3, "")
Application.SetValue("r_foot_upv.null.primary_icon", 2, "")
Application.SetValue("r_foot_upv.null.size", 0.3, "")

OperatorName = Application.FabricCanvasOpApply("null", "", True, "", "")
OperatorName = "null.kine.global.CanvasOp"

result = Application.FabricCanvasImportGraph( OperatorName, JSONFilePath )

port_map_definition = []
for x in ["R_hand", "R_elbow", "L_hand", "L_elbow", "R_foot", "R_knee", "L_foot", "L_knee"]:
    port_map_definition.append( r"{}|XSI Port".format(x))
Application.FabricCanvasOpPortMapDefine( "null.kine.global.CanvasOp", "<<->>".join(port_map_definition ))

success = Application.FabricCanvasOpConnectPort( OperatorName, "R_hand",  "r_hand_ik", False )
success = Application.FabricCanvasOpConnectPort( OperatorName, "R_elbow", "r_hand_upv", False )
success = Application.FabricCanvasOpConnectPort( OperatorName, "L_hand",  "L_hand_ik", False )
success = Application.FabricCanvasOpConnectPort( OperatorName, "L_elbow", "L_hand_upv", False )
success = Application.FabricCanvasOpConnectPort( OperatorName, "R_foot",  "r_foot_ik", False )
success = Application.FabricCanvasOpConnectPort( OperatorName, "R_knee",  "r_foot_upv", False )
success = Application.FabricCanvasOpConnectPort( OperatorName, "L_foot",  "L_foot_ik", False )
success = Application.FabricCanvasOpConnectPort( OperatorName, "L_knee",  "L_foot_upv", False )
