#if ( defined (__STDC__) || defined (__FORCE_PROTO) ) && !defined(__NO_PROTO)
# define	P_ipc(s) s
#else
# define P_ipc(s) ()
#endif


/* IPC.c */
static Ipc_Boolean_t kw_match P_ipc((char *keyword , char *str ));
Ipc_Status_t ipc_initialize_server P_ipc((char *server_name , Ipc_Mode_t m , Ipc_Protocol_t p ));
Ipc_Status_t ipc_terminate_server P_ipc((void ));
Ipc_Status_t ipc_get_line P_ipc((char *str , int *len , Ipc_Wait_t wait ));
Ipc_Status_t ipc_flush P_ipc((void ));
static Ipc_Status_t ipc_send_line_binary P_ipc((char *str , int len ));
Ipc_Status_t ipc_send_line P_ipc((char *str ));
Ipc_Status_t ipc_send_data_prefix P_ipc((double time ));
Ipc_Status_t ipc_send_dcop_prefix P_ipc((void ));
Ipc_Status_t ipc_send_data_suffix P_ipc((void ));
Ipc_Status_t ipc_send_dcop_suffix P_ipc((void ));
Ipc_Status_t ipc_send_errchk P_ipc((void ));
Ipc_Status_t ipc_send_end P_ipc((void ));
static int stuff_binary_v1 P_ipc((double d1 , double d2 , int n , char *buf , int pos ));
Ipc_Status_t ipc_send_double P_ipc((char *tag , double value ));
Ipc_Status_t ipc_send_complex P_ipc((char *tag , Ipc_Complex_t value ));
Ipc_Status_t ipc_send_int P_ipc((char *tag , int value ));
Ipc_Status_t ipc_send_boolean P_ipc((char *tag , Ipc_Boolean_t value ));
Ipc_Status_t ipc_send_string P_ipc((char *tag , char *value ));
Ipc_Status_t ipc_send_int_array P_ipc((char *tag , int array_len , int *value ));
Ipc_Status_t ipc_send_double_array P_ipc((char *tag , int array_len , double *value ));
Ipc_Status_t ipc_send_complex_array P_ipc((char *tag , int array_len , Ipc_Complex_t *value ));
Ipc_Status_t ipc_send_boolean_array P_ipc((char *tag , int array_len , Ipc_Boolean_t *value ));
Ipc_Status_t ipc_send_string_array P_ipc((char *tag , int array_len , char **value ));

Ipc_Status_t ipc_send_evtdict_prefix ();
Ipc_Status_t ipc_send_evtdict_suffix ();
Ipc_Status_t ipc_send_evtdata_prefix ();
Ipc_Status_t ipc_send_evtdata_suffix ();
Ipc_Status_t ipc_send_event(int ipc_index, double step, double plot_val, char *print_val, void *ipc_val, int len);

/* IPCtiein.c */
void ipc_handle_stop P_ipc((void ));
void ipc_handle_returni P_ipc((void ));
void ipc_handle_mintime P_ipc((double time ));
void ipc_handle_vtrans P_ipc((char *vsrc , char *dev ));
static void ipc_send_stdout P_ipc((void ));
static void ipc_send_stderr P_ipc((void ));
Ipc_Status_t ipc_send_std_files P_ipc((void ));
Ipc_Boolean_t ipc_screen_name P_ipc((char *name , char *mapped_name ));
int ipc_get_devices P_ipc((void *circuit , char *device , char ***names , double **modtypes ));
void ipc_free_devices P_ipc((int num_items , char **names , double *modtypes ));
void ipc_check_pause_stop P_ipc((void ));

/* IPCaegis.c */
Ipc_Status_t ipc_transport_initialize_server P_ipc((char *server_name , Ipc_Mode_t m , Ipc_Protocol_t p , char *batch_filename ));
static Ipc_Status_t extract_msg P_ipc((char *str , int *len ));
Ipc_Status_t ipc_transport_get_line P_ipc((char *str , int *len , Ipc_Wait_t wait ));
Ipc_Status_t ipc_transport_terminate_server P_ipc((void ));
Ipc_Status_t ipc_transport_send_line P_ipc((char *str , int len ));

#undef P_ipc
