
import textwrap

def splice(operator, command, *args, **kwargs):
    return Application.fabricSplice(command, operator, str(kwargs), *args)


def set_kl(operator, op_name, code):
    splice(operator, "addKLOperator", opName=op_name)
    splice(operator, "setKLOperatorCode", code, opName=op_name)


def draw_bones_traditional(points):
    assert len(points) >= 3
    start = points[0]
    mid   = points[1]
    end   = points[2]
    Application.Create3DSkeleton(
            start[0], start[1], start[2],
            mid[0],   mid[1], mid[2],
            end[0],   end[1], end[2],
        "", "")

    for p in points[3:]:
        x = p[0]
        y = p[1]
        z = p[2]
        Application.AppendBone("eff", x, y, z, False)




Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.Translate("", 7.21095660746,      14.9754557972,  -0.257095710115)
Application.GetPrim("Null", "", "Scene_Root", "")
Application.Translate("", -7.21079536001,     14.9612588443,  -0.2533093422)
Application.GetPrim("Null", "", "Scene_Root", "")
Application.Translate("", 1.5139886508,       0.913547291364, -0.29962025889)
Application.GetPrim("Null", "", "Scene_Root", "")
Application.Translate("", -1.5139886508,      0.913547291364, -0.299620258891)
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")
Application.GetPrim("Null", "", "Scene_Root", "")



klCode = textwrap.dedent("""
require Math;
require Characters;
require FABRIK;

require InlineDrawing;

operator initCharacter( io Skeleton skeleton, io DrawingHandle handle, io FFBIKGraph fbg, in Mat44 ik_handles[], io FABRIKResolver resolver, io Mat44 output[] ) {

  //////////////////////////////////
  // Generate a chain of bones with a random shape.



    if( skeleton.bones.size() == 0 ) {
        Bone bones[];
        bones.resize(0);
        report( "init skeleton" );
        skeleton = Skeleton("", bones);
        skeleton.addBone("root", "", Xfo() );

        skeleton.addBone("GlobalSRT",   "Biped_Nulls", Xfo( Vec3(0.0,                0.0,            0.0),              Quat(0.0,               0.0,                0.0,                1.0)),             0.0);
        skeleton.addBone("UpperBody",   "GlobalSRT",   Xfo( Vec3(0.0,                12.2661892594,  -0.654324640582),  Quat(-0.0112288597746,  0.0,                0.0,                0.999936954367)),  0.0);
        skeleton.addBone("SpineStart1", "UpperBody",   Xfo( Vec3(0.0,                12.8474815885,  -0.723259864691),  Quat(-0.0527451954048,  6.79523711605e-16,  2.48282297499e-16,  0.998608003354)),  0.0);
        skeleton.addBone("Vertebrae4",  "SpineStart1", Xfo( Vec3(-9.3677232495e-31,  14.0160906498,  -0.755619144199),  Quat(0.0317507633696,   1.21400827759e-15,  -1.33486971476e-15, 0.999495817413)),  0.0);
        skeleton.addBone("Chest",       "Vertebrae4",  Xfo( Vec3(-5.34638152562e-30, 14.5993929147,  -0.706732986485),  Quat(-0.0112288597746,  5.66993775628e-31,  8.32001735975e-31,  0.999936954367)),  0.0);
        skeleton.addBone("LShoulder",   "Chest",       Xfo( Vec3(0.545846772228,     16.8771170017,  -0.513789144856),  Quat(-0.706417695192,   -0.0389174896638,   -0.0312096132635,   0.706035005476)),  0.0);
        skeleton.addBone("LBicep",      "LShoulder",   Xfo( Vec3(1.90512094987,      16.8920261192,  -0.378481940292),  Quat(-0.715975660079,   0.0421541604979,    0.0288108890372,    0.696255566298)),  0.0);
        skeleton.addBone("LThigh",      "UpperBody",   Xfo( Vec3(0.995733296199,     11.0781917979,  -0.335466042446),  Quat(-0.532110496038,   0.454639947624,     -0.490685593649,    0.519026575636)),  0.0);
        skeleton.addBone("LShin",       "LThigh",      Xfo( Vec3(1.56874195804,      5.66121486923,  -0.0613571557273), Quat(-0.50748133935,    0.481976920797,     -0.462729820641,    0.544097464725)),  0.0);
        skeleton.addBone("LFootBone1",  "LShin",       Xfo( Vec3(2.05604300044,      1.14681057235,  -0.310701027798),  Quat(-0.674760484424,   0.211419697899,     -0.674760484424,    0.211419697899)),  0.0);
        skeleton.addBone("Neck",        "Chest",       Xfo( Vec3(-1.05098059909e-09, 16.9182283127,  -0.364639733917),  Quat(-0.0360926604749,  -4.32694865484e-09, -5.70897876621e-10, 0.99934844767)),   0.0);
        skeleton.addBone("RThigh",      "UpperBody",   Xfo( Vec3(-0.995733296199,    11.0781917979,  -0.335466042446),  Quat(-0.490685593649,   0.519026575636,     -0.532110496038,    0.454639947624)),  0.0);
        skeleton.addBone("LFootBone2",  "LFootBone1",  Xfo( Vec3(2.05604300044,      0.61760894757,  0.450884441283),   Quat(-0.688534849771,   0.160996151046,     -0.688534849771,    0.160996151046)),  0.0);
        skeleton.addBone("RShoulder",   "Chest",       Xfo( Vec3(-0.545846771806,    16.8771170026,  -0.513789154342),  Quat(0.70603500584,     0.03120960654,      -0.0389174841141,   0.706417695431)),  0.0);
        skeleton.addBone("RBicep",      "RShoulder",   Xfo( Vec3(-1.90512095178,     16.8920261223,  -0.378481973401),  Quat(-0.0421541659596,  0.715975659863,     0.696255565908,     0.0288108958289)), 0.0);
        skeleton.addBone("LForearm",    "LBicep",      Xfo( Vec3(4.88948677107,      16.8312962889,  -0.678350535737),  Quat(-0.717094865852,   -0.0131556999517,   -0.0249393344485,   0.696404990307)),  0.0);
        skeleton.addBone("RFootBone1",  "RShin",       Xfo( Vec3(-2.05604300044,     1.14681057235,  -0.310701027798),  Quat(-0.674760484424,   0.211419697899,     -0.674760484424,    0.211419697899)),  0.0);
        skeleton.addBone("RFootBone2",  "RFootBone1",  Xfo( Vec3(-2.05604300044,     0.617608947569, 0.450884441283),   Quat(-0.688534849771,   0.160996151046,     -0.688534849771,    0.160996151046)),  0.0);
        skeleton.addBone("RShin",       "RThigh",      Xfo( Vec3(-1.56874195804,     5.66121486923,  -0.0613571557273), Quat(-0.462729820641,   0.544097464725,     -0.50748133935,     0.481976920797)),  0.0);
        skeleton.addBone("RForearm",    "RBicep",      Xfo( Vec3(-4.88948676787,     16.831296297,   -0.678350620703),  Quat(-0.0131556944913,  -0.717094866058,    -0.696404990442,    0.0249393276485)), 0.0);
        skeleton.addBone("Head",        "Neck",        Xfo( Vec3(-5.80146677849e-10, 18.4182283119,  -0.436966459513),  Quat(-0.0120525440086,  -5.27179780071e-09, -4.55345641655e-10, 0.999927365454)),  0.0);
        skeleton.addBone("LHand",       "LForearm",    Xfo( Vec3(7.88471079473,      16.7836924274,  -0.516077462863),  Quat(0.000877373200168, 0.0349317417593,    -0.0251334107165,   0.999073228197)),  0.0);
        skeleton.addBone("RHand",       "RForearm",    Xfo( Vec3(-7.88471079766,     16.7836924355,  -0.516077551539),  Quat(-0.0251334101996,  0.999073228014,     0.000877372859551,  0.0349317473689)), 0.0);

        fbg = FFBIKGraph( skeleton );
        // upper body triangle
        fbg.addEdge( "Chest", "LBicep" );
        fbg.addEdge( "Chest", "RBicep" );
        fbg.addEdge( "LBicep",   "RBicep" );
        fbg.addEdge( "LBicep",   "Head" );
        fbg.addEdge( "RBicep",   "Head" );
        // lower body 
        fbg.addEdge( "Chest", "LThigh" );
        fbg.addEdge( "Chest", "RThigh" );
        fbg.addEdge( "LThigh",   "RThigh" );
        // leg
        fbg.addEdge( "LThigh",   "LShin" );
        fbg.addEdge( "LShin",    "LFootBone1" );
        fbg.addEdge( "RThigh",   "RShin" );
        fbg.addEdge( "RShin",    "RFootBone1" );
        // arm
        fbg.addEdge( "LBicep",   "LForearm" );
        fbg.addEdge( "LForearm", "LHand" );
        fbg.addEdge( "RBicep",   "RForearm" );
        fbg.addEdge( "RForearm", "RHand" );
        fbg.addEdge( "Chest", "Head" );
        fbg.setRootNode( "Chest" );
        fbg.finalize();
        fbg.reportNodes();


        FFBIKPose pose = FFBIKPose(skeleton);
        for ( Index i=0; i < skeleton.bones.size; i++){
            report(i +":    "+ skeleton.getBone( i ).name );
        }

        resolver = FABRIKResolver( skeleton, fbg );
        addArmSolver( resolver, fbg, skeleton, handle, "Chest", "LBicep", "LForearm", "LHand");
        addArmSolver( resolver, fbg, skeleton, handle, "Chest", "RBicep", "RForearm", "RHand");
        addLegSolver( resolver, fbg, skeleton, handle, "Chest", "LThigh", "LShin", "LFootBone1");
        addLegSolver( resolver, fbg, skeleton, handle, "Chest", "RThigh", "RShin", "RFootBone1");
        addSpineSolver( resolver, fbg, skeleton, handle, "Chest", "LBicep", "RBicep", "LThigh", "RThigh" );

    }  
    FFBIKPose pose = FFBIKPose(skeleton);
    resolver.solve( IPose( pose ), ik_handles );
    fbg.drawEdges( ISkeleton(skeleton), IPose(pose), handle );
    fbg.drawNodes( ISkeleton(skeleton), IPose(pose), handle );
    //drawSkeleton( ISkeleton(skeleton), IPose(pose), handle.getRootTransform() );

    /*
    for (Index i=0; i < output.size; i++ ){
        output[i] = pose.getBoneXfo(i).toMat44();
    }
    */

}
""")






#xsi_man = XSIUtils.ResolvePath( Application.GetInstallationPath2(3) + "\\Data\\XSI_SAMPLES\\Models\\Characters\\XSI_Man.emdl")
bip_man = XSIUtils.ResolvePath( Application.GetInstallationPath2(3) + "\\Data\\XSI_SAMPLES\\Models\\Characters\\Biped_Nulls.emdl")
Application.ImportModel(bip_man, "", "", "", "", "", "")

op = Application.fabricSplice("newSplice", '''
{
    "portMode": "io",
    "portName": "result",
    "targets": "null.kine.global"
}
''')





b = "null6.kine.global,Biped_Nulls.GlobalSRT.kine.global,Biped_Nulls.UpperBody.kine.global,Biped_Nulls.SpineStart1.kine.global,Biped_Nulls.Vertebrae4.kine.global,Biped_Nulls.Chest.kine.global,Biped_Nulls.LShoulder.kine.global,Biped_Nulls.LBicep.kine.global,Biped_Nulls.LThigh.kine.global,Biped_Nulls.LShin.kine.global,Biped_Nulls.LFootBone1.kine.global,Biped_Nulls.Neck.kine.global,Biped_Nulls.RThigh.kine.global,Biped_Nulls.LFootBone2.kine.global,Biped_Nulls.RShoulder.kine.global,Biped_Nulls.RBicep.kine.global,Biped_Nulls.LForearm.kine.global,Biped_Nulls.RFootBone1.kine.global,Biped_Nulls.RFootBone2.kine.global,Biped_Nulls.RShin.kine.global,Biped_Nulls.RForearm.kine.global,Biped_Nulls.Head.kine.global,Biped_Nulls.LHand.kine.global,Biped_Nulls.RHand.kine.global"
b = "null6.kine.global,null7.kine.global,null8.kine.global,null9.kine.global,null10.kine.global,null11.kine.global,null12.kine.global,null13.kine.global,null14.kine.global,null15.kine.global,null16.kine.global,null17.kine.global,null18.kine.global,null19.kine.global,null20.kine.global,null21.kine.global,null22.kine.global,null23.kine.global,null24.kine.global,null25.kine.global,null26.kine.global,null27.kine.global,null28.kine.global,null29.kine.global"

splice(op, "addInternalPort", portName="skeleton",    dataType="Skeleton",       portMode="IO", extension="Characters")
splice(op, "addInternalPort", portName="handle",      dataType="DrawingHandle",  portMode="IO", extension="InlineDrawing")
splice(op, "addInternalPort", portName="fbg",         dataType="FFBIKGraph",     portMode="IO", extension="FABRIK")
splice(op, "addInternalPort", portName="resolver",    dataType="FABRIKResolver", portMode="IO", extension="FABRIK")
splice(op, "addInputPort",    portName="ik_handles", dataType="Mat44[]",        portMode="IO", extension="", targets="null1.kine.global,null2.kine.global,null3.kine.global,null4.kine.global,null5.kine.global,null6.kine.global")
splice(op, "addOutputPort",   portName="output",     dataType="Mat44[]",        extension="",targets=b)
set_kl(op, "initCharacter", klCode)
