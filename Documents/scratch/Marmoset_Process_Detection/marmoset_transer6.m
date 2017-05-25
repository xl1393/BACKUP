fid = fopen('/home/xli/Documents/scratch/Marmoset_Process_Detection/filelist6.txt');
tline=fgets(fid);
while ischar(tline)
    filepath=strcat('/nfs/data/main/M25/marmosetRIKEN/NZ/m919/m919F/M919XXL/',tline);
    disp(filepath)
    img=imread(filepath);
    savefilepath=strcat('/home/xli/Documents/scratch/Marmoset919MAT/',tline,'.mat');
    save(savefilepath,'img','-V7.3');
    disp(savefilepath)
    tline=fgets(fid);
end

fclose(fid);