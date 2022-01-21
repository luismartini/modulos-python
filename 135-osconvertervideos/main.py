# https://ffmpeg.zeranoe.com/builds/

'''
ffmpeg -i "Entrada" -i "LEGENDA" -c:v libx264 -crf 23 -preset ultrafast -c:a aac -b:a 320k -c:srt -map v:0 a -map 1:0 -ss 00:00:00 -to 00:00:10 "SAÍDA"
'''
import os
import fnmatch
import sys

if sys.platform == 'windows':
    # comando_ffmpeg = 'ffmpeg'
    pass
else:
    comando_ffmpeg = r'D:\udemy-python\est\modulos-python\os\ffmpeg\ffmpeg.exe'

codec_video = '-c:v libx264'
crf = '-crf 23'
preset = '-preset ultrafast'
codec_audio = '-c:a aac'
bitrate_audio = '-b:a 320k'
debug = '-ss 00:00:00 -to 00:00:10'

caminho_origem = r'C:\Users\luisl\Desktop\video'
caminho_destino = r'C:\Users\luisl\Desktop\video1'

for raiz, pastas, arquivos in os.walk(caminho_origem):
    for arquivo in arquivos:
        if not fnmatch.fnmatch(arquivo, '*.mp4'):
            continue
        
        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, extensao_arquivo = os.path.splitext(caminho_completo)
        caminho_legenda = nome_arquivo + '.str'
        
        if os.path.isfile(caminho_legenda):
            input_legenda = f'-i "{caminho_legenda}"'
            map_legenda = '-c:s srt -map v:0 -map a -map 1:0'
        else:
            input_legenda = ''
            map_legenda = ''
        
        nome_novo_arquivo = nome_arquivo + '_NOVO' + extensao_arquivo
        nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
        
        arquivo_saída = f'{caminho_destino}/{arquivo} NOVO{extensao_arquivo}'
        
        comando = f'{comando_ffmpeg} -i "{caminho_completo}" {input_legenda} {codec_video} {crf} {preset} {codec_audio} {bitrate_audio} {map_legenda} {debug} "{arquivo_saída}"'
        
        os.system(comando)