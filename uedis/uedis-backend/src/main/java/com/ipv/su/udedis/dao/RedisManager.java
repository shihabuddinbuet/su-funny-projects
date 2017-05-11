package com.ipv.su.udedis.dao;

import java.io.IOException;
import java.util.HashSet;
import java.util.Set;

import redis.clients.jedis.HostAndPort;
import redis.clients.jedis.JedisCluster;

public class RedisManager {
	private static final String HOST = "localhost";
	private static final int PORT = 7000;
	
	private static JedisCluster connection = null;
	
	private RedisManager() {
		//nop
	}
	
	public static JedisCluster getConnection() {
		return connection == null ? createConnection() : connection;
	}
	
	private static JedisCluster createConnection() {
		Set<HostAndPort> hpSet = new HashSet<HostAndPort>();
		hpSet.add(new HostAndPort(HOST, PORT));
		return new JedisCluster(hpSet);
	}
	
	public static void close() {
		if(connection != null) {
			try {
				connection.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
 }
