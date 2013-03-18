@echo OFF
convert_rmxp_2_arc.rb RMXP_original ARC_imported
convert_arc_2_rmxp.rb ARC_imported RMXP_imported
compare.rb RMXP_original RMXP_imported
pause