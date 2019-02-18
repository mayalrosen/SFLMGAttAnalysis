
# coding: utf-8

import math, os, sys, random, csv, itertools
subjects = []

def getsubject(row):
    subject = row[1]
    return subject
BLOCKTYPE = 20
MGATTPROBE_ACC = 31
MGATTPROBE_RT = 38
MGATTRESP_ACC = 40
MGATTRESP_RT = 47
STIMPROBE_ACC = 88
STIMPROBE_RT = 95
STIMRESP_ACC = 97
STIMRESP_RT = 104
VALIDINVALID = 120
output_row = []
headers = ["Subject", "valid_MGA_prop_corr", "invalid_MGA_prop_corr", "valid_STIM_prop_corr", "invalid_STIM_prop_corr", "valid_MGA_RT", "invalid_MGA_RT", "valid_STIM_RT", "invalid_STIM_RT"]
filepath = '/Users/mayarosen/Documents/MGAttSpreadsheetSFLREDUCED.csv'
output_filename = "/Users/mayarosen/Desktop/SFL_MGA_Output.csv"
with open(output_filename,"wb") as outfile_handle:
    csv_writer = csv.writer(outfile_handle)
    csv_writer.writerow(headers)
    with open(filepath,'rU') as fh:
        reader = csv.reader(fh)
        next(reader)
        subjects = itertools.groupby(reader, key = getsubject)
        for row in subjects:
            subject_id, data = row[0], row[1]
            records = list(data)
            validMGAcorrectResponse = 0
            invalidMGAcorrectResponse = 0
            validSTIMcorrectResponse = 0
            invalidSTIMcorrectResponse = 0
            validMGAresponse_time = 0
            invalidMGAresponse_time = 0
            validSTIMresponse_time = 0
            invalidSTIMresponse_time = 0
            for record in records:  
                if record[BLOCKTYPE] == "MGAtt":
                    if record[VALIDINVALID] == "valid":
                        if int(record[MGATTPROBE_ACC]) == 1:
                            validMGAcorrectResponse +=1
                            validMGAresponse_time = validMGAresponse_time + float(record[MGATTPROBE_RT])
                        elif int(record[MGATTPROBE_ACC]) == 0:
                            if int(record[MGATTRESP_ACC]) == 1:
                                validMGAcorrectResponse +=1
                                validMGAresponse_time = validMGAresponse_time + (float(record[MGATTRESP_RT]) + 500)
                    if record[VALIDINVALID] == "invalid":
                        if int(record[MGATTPROBE_ACC]) == 1:
                            invalidMGAcorrectResponse +=1
                            invalidMGAresponse_time = invalidMGAresponse_time + float(record[MGATTPROBE_RT])
                        elif int(record[MGATTPROBE_ACC]) == 0:
                            if int(record[MGATTRESP_ACC]) == 1:
                                invalidMGAcorrectResponse +=1
                                invalidMGAresponse_time = invalidMGAresponse_time + (float(record[MGATTRESP_RT]) + 500)
                            #print "THIS IS MGA CORRECT RESPOSNE", MGAcorrectResponse
                if record[BLOCKTYPE] == "STIM":
                    if record[VALIDINVALID] == "valid":
                        if int(record[STIMPROBE_ACC]) == 1:
                            validSTIMcorrectResponse +=1
                            validSTIMresponse_time = validSTIMresponse_time + float(record[STIMPROBE_RT])
                        elif int(record[STIMPROBE_ACC]) == 0:
                            if int(record[STIMRESP_ACC]) == 1:
                                validSTIMcorrectResponse +=1
                                validSTIMresponse_time = validSTIMresponse_time + (float(record[STIMRESP_RT]) + 500)
                    if record[VALIDINVALID] == "invalid":
                        if int(record[STIMPROBE_ACC]) == 1:
                            invalidSTIMcorrectResponse +=1
                            invalidSTIMresponse_time = invalidSTIMresponse_time + float(record[STIMPROBE_RT])
                        elif int(record[STIMPROBE_ACC]) == 0:
                            if int(record[STIMRESP_ACC]) == 1:
                                invalidSTIMcorrectResponse +=1
                                invalidSTIMresponse_time = invalidSTIMresponse_time + (float(record[STIMRESP_RT]) + 500)
            prop_corr_validMGA = float(validMGAcorrectResponse) / 16
            prop_corr_invalidMGA = float(invalidMGAcorrectResponse) / 16
            prop_corr_validSTIM = float(validSTIMcorrectResponse) / 16
            prop_corr_invalidSTIM = float(invalidSTIMcorrectResponse) / 16
            valid_avg_MGAResponse_time = validMGAresponse_time / validMGAcorrectResponse
            invalid_avg_MGAResponse_time = invalidMGAresponse_time / invalidMGAcorrectResponse
            valid_avg_StimResponse_time = validSTIMresponse_time / validSTIMcorrectResponse
            invalid_avg_StimResponse_time = invalidSTIMresponse_time / invalidSTIMcorrectResponse

            output_row.append(subject_id)
            output_row.append(prop_corr_validMGA)
            output_row.append(prop_corr_invalidMGA)
            output_row.append(prop_corr_validSTIM) 
            output_row.append(prop_corr_invalidSTIM) 
            output_row.append(valid_avg_MGAResponse_time)
            output_row.append(invalid_avg_MGAResponse_time)
            output_row.append(valid_avg_StimResponse_time)
            output_row.append(invalid_avg_StimResponse_time)
            
        
            csv_writer.writerow(output_row)
            #print subject_id, prop_corr_validMGA, prop_corr_invalidMGA, prop_corr_validSTIM, prop_corr_invalidSTIM, valid_avg_MGAResponse_time, invalid_avg_MGAResponse_time, valid_avg_StimResponse_time, invalid_avg_StimResponse_time
