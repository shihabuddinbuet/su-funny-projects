package com.ipv.su.uedis;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@Path("/api")
public class UedisApi {
	
	@GET
	@Path("/keys")
	@Produces(MediaType.APPLICATION_JSON)
	public Response getKeys() {
		System.out.println("got request ............");
		return Response.ok().build();
	}
	
}
