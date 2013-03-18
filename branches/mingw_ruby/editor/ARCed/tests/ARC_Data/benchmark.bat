@echo OFF
convert_rmxp_2_arc.rb RMXP_original arc_d
convert_arc_2_rmxp.rb arc_d rmxp_d
echo - removing temporary data...
rmdir /S /Q arc_d
rmdir /S /Q rmxp_d
pause