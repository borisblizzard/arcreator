#==============================================================================
# Interpreter (2)
#==============================================================================

class Interpreter
  
  def execute_command
    if @index >= @list.size - 1
      command_end
      return true
    end
    @parameters = @list[@index].parameters
    case @list[@index].code
    when 101 then return command_101
    when 102 then return command_102
    when 402 then return command_402
    when 403 then return command_403
    when 103 then return command_103
    when 104 then return command_104
    when 105 then return command_105
    when 106 then return command_106
    when 111 then return command_111
    when 411 then return command_411
    when 112 then return command_112
    when 413 then return command_413
    when 113 then return command_113
    when 115 then return command_115
    when 116 then return command_116
    when 117 then return command_117
    when 118 then return command_118
    when 119 then return command_119
    when 121 then return command_121
    when 122 then return command_122
    when 123 then return command_123
    when 124 then return command_124
    when 125 then return command_125
    when 126 then return command_126
    when 127 then return command_127
    when 128 then return command_128
    when 129 then return command_129
    when 131 then return command_131
    when 132 then return command_132
    when 133 then return command_133
    when 134 then return command_134
    when 135 then return command_135
    when 136 then return command_136
    when 201 then return command_201
    when 202 then return command_202
    when 203 then return command_203
    when 204 then return command_204
    when 205 then return command_205
    when 206 then return command_206
    when 207 then return command_207
    when 208 then return command_208
    when 209 then return command_209
    when 210 then return command_210
    when 221 then return command_221
    when 222 then return command_222
    when 223 then return command_223
    when 224 then return command_224
    when 225 then return command_225
    when 231 then return command_231
    when 232 then return command_232
    when 233 then return command_233
    when 234 then return command_234
    when 235 then return command_235
    when 236 then return command_236
    when 241 then return command_241
    when 242 then return command_242
    when 245 then return command_245
    when 246 then return command_246
    when 247 then return command_247
    when 248 then return command_248
    when 249 then return command_249
    when 250 then return command_250
    when 251 then return command_251
    when 301 then return command_301
    when 601 then return command_601
    when 602 then return command_602
    when 603 then return command_603
    when 302 then return command_302
    when 303 then return command_303
    when 311 then return command_311
    when 312 then return command_312
    when 313 then return command_313
    when 314 then return command_314
    when 315 then return command_315
    when 316 then return command_316
    when 317 then return command_317
    when 318 then return command_318
    when 319 then return command_319
    when 320 then return command_320
    when 321 then return command_321
    when 322 then return command_322
    when 331 then return command_331
    when 332 then return command_332
    when 333 then return command_333
    when 334 then return command_334
    when 335 then return command_335
    when 336 then return command_336
    when 337 then return command_337
    when 338 then return command_338
    when 339 then return command_339
    when 340 then return command_340
    when 351 then return command_351
    when 352 then return command_352
    when 353 then return command_353
    when 354 then return command_354
    when 355 then return command_355
    else
      return true
    end
  end
  
  def command_end
    @list = nil
    if $game_map.events != nil && $game_map.events[@event_id] != nil
      $game_map.events[@event_id].unlock if @main && @event_id > 0
    end
  end
  
  def command_skip
    indent = @list[@index].indent
    loop do
      return true if @list[@index+1].indent == indent
      @index += 1
    end
  end
  
  def get_character(parameter)
    return case parameter
    when -1 then $game_player
    when 0 then ($game_map.events == nil ? nil : $game_map.events[@event_id])
    else
      ($game_map.events == nil ? nil : $game_map.events[parameter])
    end
  end
  
  def operate_value(operation, operand_type, operand)
    value = (operand_type == 0 ? operand : $game_variables[operand])
    value = -value if operation == 1
    return value
  end
  
end
